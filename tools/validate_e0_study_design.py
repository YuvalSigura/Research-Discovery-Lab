"""Review-only E0 preregistration design checker; NEVER a performance qualification.

Checks reported metadata for independence, unseen-category holdout, placebo
length matching, approximate paired normal-design power and double-rating plan.
Cannot authenticate authorship, ratings, original source lineage or blinding.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from statistics import NormalDist


ARMS = ["baseline", "rdl_relevant", "rdl_unrelated"]
HEX_SHA256 = re.compile(r"^[a-f0-9]{64}$")
TASK_ID = re.compile(r"^[a-f0-9]{24}$")


def _nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def _sha(value):
    return isinstance(value, str) and bool(HEX_SHA256.fullmatch(value))


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_design(payload: dict) -> dict:
    _require(isinstance(payload, dict) and
             payload.get("format") == "rdl.e0.preregistered_design.v1",
             "Expected rdl.e0.preregistered_design.v1 object")
    _require(payload.get("arms") == ARMS, "Wrong E0 arm list")
    for name in ("preregistration_id", "model_revision", "tokenizer_revision",
                 "retrieval_corpus_revision", "fixture_set_revision"):
        _require(_nonblank(payload.get(name)), "Missing frozen metadata: " + name)
    for name in ("base_prompt_sha256", "retrieval_corpus_sha256", "fixture_manifest_sha256"):
        _require(_sha(payload.get(name)), "Missing/invalid SHA-256 freeze: " + name)
    decoding = payload.get("decoding_parameters")
    _require(isinstance(decoding, dict) and bool(decoding) and
             all(_nonblank(k) for k in decoding),
             "Decoding parameters must be pinned")
    _require(type(payload.get("context_window_tokens")) is int and
             payload["context_window_tokens"] > 0, "Context window must be pinned")

    authors = payload.get("authors", {})
    _require(isinstance(authors, dict), "Missing authorship declaration")
    for key in ("ontology", "retrieval_guidance", "fixture", "reviewer"):
        ids = authors.get(key)
        _require(isinstance(ids, list) and bool(ids) and
                 all(_nonblank(x) for x in ids) and len(ids) == len(set(ids)),
                 "Missing/duplicate author identifiers for " + key)
    _require(not set(authors["fixture"]) & (set(authors["ontology"]) |
                                          set(authors["retrieval_guidance"])),
             "Fixture authors cannot author ontology or guidance")
    _require(not set(authors["reviewer"]) & (
        set(authors["fixture"]) | set(authors["ontology"]) |
        set(authors["retrieval_guidance"])),
        "Independent reviewers cannot author study fixtures or guidance")
    attest = payload.get("independence_attestations", {})
    for k in ("fixture_authors_blind_to_ontology", "reviewers_blind_to_arms",
              "hidden_keys_separated", "source_near_duplicate_screened"):
        _require(isinstance(attest, dict) and attest.get(k) is True,
                 "Missing independent study attestation: " + k)
    _require(_nonblank(payload.get("independent_fixture_protocol_ref")),
             "Independent fixture protocol reference required")

    power = payload.get("power_plan", {})
    _require(isinstance(power, dict), "Missing paired power plan")
    for k in ("two_sided_alpha", "target_power", "minimum_detectable_difference",
              "assumed_paired_difference_sd", "anticipated_attrition_fraction"):
        v = power.get(k)
        _require(type(v) in (float, int) and math.isfinite(v),
                 "Invalid power_plan: " + k)
    _require(0 < power["two_sided_alpha"] <= 0.05, "Invalid alpha")
    _require(0.8 <= power["target_power"] < 1, "Power target below 80%")
    _require(power["minimum_detectable_difference"] > 0 and
             power["assumed_paired_difference_sd"] > 0, "MDE/SD must be positive")
    _require(0 <= power["anticipated_attrition_fraction"] < 0.5,
             "Invalid planned attrition")
    _require(power.get("multiplicity") == "bonferroni_two_primary_contrasts",
             "Primary contrast multiplicity must be preplanned")
    _require(_nonblank(power.get("assumptions_basis")) and
             _nonblank(power.get("cluster_dependence_review")),
             "Power assumptions and family/lineage dependence must be documented")
    zalpha = NormalDist().inv_cdf(1 - power["two_sided_alpha"] / 4)
    zbeta = NormalDist().inv_cdf(power["target_power"])
    mde = power["minimum_detectable_difference"]
    sd = power["assumed_paired_difference_sd"]
    min_n = math.ceil(((zalpha + zbeta) * sd / mde) ** 2)
    attrition_adjusted_n = math.ceil(min_n / (1 - power["anticipated_attrition_fraction"]))

    tasks = payload.get("fixtures")
    _require(isinstance(tasks, list) and bool(tasks), "No blinded controlled fixtures")
    ids = set()
    unseen_cats = set()
    blind_count = 0
    for f in tasks:
        _require(isinstance(f, dict), "Bad fixture record")
        fid = f.get("opaque_task_id")
        _require(isinstance(fid, str) and TASK_ID.fullmatch(fid) and fid not in ids,
                 "Duplicate/invalid opaque fixture identifier")
        ids.add(fid)
        _require(f.get("fixture_author_id") in authors["fixture"],
                 "Fixture author not declared independent")
        _require(_sha(f.get("fixture_digest_sha256")), "Missing frozen fixture digest")
        _require(f.get("source_lineage_separation_reviewed") is True,
                 "Fixture lineage separation missing")
        _require(f.get("gold_answer_key_sealed") is True,
                 "Fixture answer-key sealing missing")
        _require(f.get("taxonomy_holdout") in (True, False),
                 "Unknown blind-category status")
        if f["taxonomy_holdout"]:
            cat = f.get("hidden_category_id")
            _require(_nonblank(cat) and not cat.startswith(("CQ-", "TB-", "QPT-")),
                     "Unseen categories cannot be existing ontology IDs")
            unseen_cats.add(cat)
            blind_count += 1
        guidance = f.get("guidance", {})
        _require(isinstance(guidance, dict), "Missing guidance comparison")
        for a in ("rdl_relevant", "rdl_unrelated"):
            item = guidance.get(a)
            _require(isinstance(item, dict) and _sha(item.get("sha256")) and
                     type(item.get("token_count")) is int and item["token_count"] > 0,
                     "Missing hashed/token-counted placebo guidance: " + a)
        r = guidance["rdl_relevant"]["token_count"]
        u = guidance["rdl_unrelated"]["token_count"]
        _require(abs(r - u) / max(r, u) <= 0.05,
                 "Placebo/relevant guidance token length mismatch (>5%)")
    n = len(tasks)
    _require(n >= attrition_adjusted_n,
             "Insufficient planned independent paired tasks for stated approximate power")
    _require(blind_count >= math.ceil(n / 4) and len(unseen_cats) >= 2,
             "Need >=25% holdout tasks spanning >=2 genuinely unseen categories")

    rating = payload.get("rating_plan", {})
    _require(isinstance(rating, dict), "Missing independent rating plan")
    _require(rating.get("agreement_metric") in
             ("quadratic_weighted_cohen_kappa", "ordinal_krippendorff_alpha"),
             "Missing preregistered ordinal IRR metric")
    target = rating.get("minimum_acceptable_agreement")
    _require(type(target) in (float, int) and 0.0 < target <= 1.0,
             "Missing IRR acceptability threshold")
    _require(rating.get("confidence_interval_method") and
             rating.get("low_agreement_disposition") in
             ("no_go", "inconclusive_and_retrain_reviewers"),
             "Missing IRR confidence interval or poor-agreement procedure")
    double_ids = rating.get("planned_double_rated_task_ids")
    _require(isinstance(double_ids, list) and len(double_ids) == len(set(double_ids))
             and set(double_ids) <= ids and
             len(double_ids) >= math.ceil(n / 4),
             "Double rating below 25% or invalid task IDs")
    _require(len(authors["reviewer"]) >= 2, "At least two independent reviewers required")
    return {
        "format": "rdl.e0.design_check.v1",
        "qualification": "DESIGN_METADATA_CHECK_ONLY_NOT_POWER_OR_BLIND_VALIDATION",
        "planned_paired_tasks": n,
        "approximate_independent_n_floor": attrition_adjusted_n,
        "unseen_category_families_declared": len(unseen_cats),
        "unseen_category_task_count": blind_count,
        "double_rated_task_count_planned": len(double_ids),
        "claims_not_verified": [
            "Authorship, source independence, hidden-category novelty, blinded access",
            "Empirical paired-score variance, power assumptions, examiner IRR",
            "Qualified improvement, confidence intervals, causal transfer, training approval"
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("preregistered_manifest", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.preregistered_manifest.read_text(encoding="utf-8"))
        print(json.dumps(validate_design(payload), indent=2))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
