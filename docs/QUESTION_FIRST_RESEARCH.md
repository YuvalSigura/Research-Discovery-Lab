# Question-first research intelligence: from checklists to underlying questions

## Thesis

Many valuable discoveries are the outcome of reliable established checklists. A zero-day can be discovered through routine actions, and an ingenious or novel research question can end with a negative result. **We must not equate impact, originality and mindset.**

More importantly, an apparently original research *move* may be a new implementation of a research question shared across many expert investigations. Our object of study is the **research question and its origins**, not a personality label assigned to the researcher.

## Analytic graph

\`\`\`text
Historical context + assumptions + available evidence
                 |
     Observation / anomaly / failed test
                 |
          Research Question (EVT)
         /           |          \
 Hypothesis      Decision       Constraint
         \           |          /
         Research Move (EVT) -- Mindset observation (MND)
                  |               |
               Experiment         +-- novelty relative to prior art
                  |
        Positive / negative / inconclusive evidence
                  |
         New Question / Pivot  --> ... (branching DAG)

       Research Question (EVT)  -- QMP --  Umbrella Question (QPT)
        from case A                 |
        from case B                 +-- curated only if SAME CORE question
        from case C                 +-- otherwise overlap/analogy stays separate
\`\`\`

A mindset label describes an **observable research move**, not an immutable kind of person. A case can contain checklist testing, anomaly follow-up and fundamental assumption challenging. The historical researcher’s stated motive is different from an analyst’s reconstruction of their motive.

### Five independent dimensions

1. **Question:** What uncertainty did the researcher try to reduce? Which observation or failed trial brought the question about? Map to historical EVT; use \`trace\` for cited causal edges.
2. **Research move / strategy:** What did the researcher actually do? MND key from \`ontology/common/research_mindsets.json\`, linked to one or more EVT action and question nodes.
3. **Originality:** Was this a conventional method, adaptation, recombination or originality *candidate*? This is assessed **relative to the question** and prior art, never inferred from the outcome.
4. **Umbrella question:** Does the concrete question instantiate the same abstract, falsifiable uncertainty as questions in other cases? QMP relates the actual question to a versioned QPT. Multiple mappings are allowed.
5. **Outcome:** Was a zero-day claimed, independently corroborated, not found, disputed or unassessed? This is a separately reviewed CASE outcome and not evidence for any item above.

For example, fuzzing and careful manual code analysis could both test whether two parsers interpret the same message differently. This is one **possible recurring question** despite different techniques. Whether that genuinely unifies two specific investigations is a curation decision, supported with quotes/locators, not a string-similarity match.

## Data contracts (append-only, open-world)

- \`registry/mindsets/\` and \`schemas/v2/mindset.schema.json\`: strategy observations must link back to \`question_event_refs\` and underlying research \`event_refs\`. Documented motivation requires \`question_relation_refs\` for direct cited relations. Inferred links use \`analyst_hypothesis\` and never qualify as historical observations.
- \`registry/question_patterns/\` and \`schemas/v2/question_pattern.schema.json\`: open vocabulary of versioned umbrella research questions; include explicit *inclusion* and *exclusion* criteria, assumptions, source evidence and curator review. There is no fixed number of families.
- \`registry/question_mappings/\` and \`schemas/v2/question_mapping.schema.json\`: mapping from a specific historical question to an abstract QPT. Differentiate \`same_core_question\`, \`specialization\`, \`partial_overlap\`, \`analogy_only\` and \`unresolved\`. The latter three **never count as convergence**.
- \`ontology/common/research_question_hypotheses.json\`: possible seed themes for discovery and negative-example construction. **Not** a fixed classifier; truly new question classes must remain possible.
- CASE \`discovery_assessment\`: separate, reviewer-controlled zero-day status, anchored in explicit source provenance and independent verification for a corroborated claim.

A \`QMP\` mapping also records \`question_novelty\` and its basis. We should often find a **novel framing of a known question** or a **familiar question answered by a new technique**; these are different insights. Candidate new questions require a declared earlier prior-art cutoff and source comparison. Claims can be disputed or superseded; mapped definitions are pinned to a revision so a pattern cannot silently be redefined.

## CLI: operational interfaces

\`\`\`bash
python -m research_engine questions CASE-000055
python -m research_engine questions CASE-000055 --view all
python -m research_engine question-convergence --min-cases 2
python -m research_engine question-convergence --view all
python -m research_engine compare-questions CASE-000055 CASE-000001
python -m research_engine reconstruct CASE-000055
\`\`\`

\`historical\` includes only documented research questions and observed strategies with explicit causal motivation; patterns additionally require curated mapping and reviewed pattern definition. \`all\` includes inferred motives and tentative umbrella questions, **marked as such**.

For an empty mapping registry, correct output is **unmapped research questions**, not synthetic umbrella clusters. Source archives can populate historical EVT questions before any MND or QMP labels exist. This is expected and useful coverage information.

## How to discover a genuinely small set of research questions

The number of umbrella questions is an empirical hypothesis, not a project configuration.

1. Sample full investigations across product classes, research styles, published successes, negative results, and failed/inconclusive research. Include multiple research groups to avoid memorizing one lab's terminology.
2. Reconstruct questions and decisions at **the time they occurred**; anchor each to the earliest available observation or recorded explanation.
3. Inspect apparently novel moves **through their motivating question**. First assign the concrete question; independently assess the move's novelty and plausible earlier questions/methods.
4. Compare **what observation would falsify the underlying question** in both cases. Equivalent tests/invariants support a shared QPT; merely similar titles, payloads or tooling do not.
5. Require curators to document mismatch/counterexamples and negative analogues. If the abstraction loses an essential boundary or mechanism, keep separate QPTs.
6. Test recurring patterns on held-out research groups, older time slices and not-yet-disclosed studies. New uncategorized questions are positive evidence that the ontology needs revision, not a classification failure to hide.
7. Evaluate whether the same core questions **recur** and are **useful for prioritization**. Do not claim a question **caused** a zero-day from published correlations.

### Bias / leakage controls

- **Survivorship:** zero-day writeups disproportionately report successful pivots; the nonpublication of an attempt is *unknown*, not *failure*.
- **Hindsight:** published final findings cannot be used to label what was knowable before the discovery. Pre-discovery snapshots in the retrieval engine remain stricter than retrospectives.
- **Researcher expertise:** no ranking or claims about a person's intrinsic intellect. If examining expert versus novice behavior later, require a defensible, separately sourced expertise definition.
- **Nonindependence:** different articles about one case, multiple moves by the same investigator and repeated variants must not be treated as independent discovery outcomes.
- **Attribution:** 'researcher explicitly said X motivated Y' and 'we think X motivated Y' are separate provenance classes.
- **Novelty scope:** a new exploitation technique can still test a previously known scientific question. Equally, a recurring method can be used to ask a genuinely new question.

## Test boundaries

Offline synthetic tests intentionally show two very different strategies (a routine checklist and a recombined method) mapped to the **same QPT**, with *different* independently annotated outcomes. They also show an analogy that is **not** merged, a curator mapping that is distinct from an algorithmic suggestion, and an apparent originality claim held out of historical mode because the motive is analyst-inferred.

No fictitious test story is ever copied into source registries as historical evidence. The code does not train or fine-tune a model.
