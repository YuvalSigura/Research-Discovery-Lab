"""Command-line interface for source-grounded retrieval. All output is JSON."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import ResearchRetrievalEngine, ResearchStore


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m research_engine",
        description="Search and reconstruct recorded research evidence without invented history.")
    parser.add_argument("--root", type=Path, default=None, help="Repository root")
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search", help="Lexical/structured search over archived records")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--kind", action="append", dest="kinds",
                        help="Record type; may be repeated")
    search.add_argument("--case-id")
    search.add_argument("--source-id")
    search.add_argument("--publisher")
    search.add_argument("--domain")
    search.add_argument("--case-kind")
    search.add_argument("--limit", type=int, default=20)
    reconstruction = commands.add_parser("reconstruct", help="Chronology and evidence pack")
    reconstruction.add_argument("case_id")
    reconstruction.add_argument("--view", choices=["historical", "all", "pre_discovery"],
                                default="historical")
    reconstruction.add_argument("--cutoff", help="Required for pre_discovery: ISO timestamp")
    trace = commands.add_parser("trace", help="Evidence-backed predecessors of a question")
    trace.add_argument("case_id")
    trace.add_argument("question_id")
    trace.add_argument("--view", choices=["historical", "all"], default="historical")
    trace.add_argument("--depth", type=int, default=6)
    questions = commands.add_parser("questions", help="Link researcher moves and novelty to motivating questions")
    questions.add_argument("case_id")
    questions.add_argument("--view", choices=["historical", "all"], default="historical")
    convergence = commands.add_parser("question-convergence", help="Evidence-curated recurring umbrella questions across cases")
    convergence.add_argument("--view", choices=["historical", "all"], default="historical")
    convergence.add_argument("--min-cases", type=int, default=1)
    convergence.add_argument("--limit", type=int, default=100)
    compare = commands.add_parser("compare-questions", help="Compare the underlying research questions in two or more cases")
    compare.add_argument("case_ids", nargs="+")
    compare.add_argument("--view", choices=["historical", "all"], default="historical")
    related = commands.add_parser("related", help="Explicitly linked investigations")
    related.add_argument("case_id")
    related.add_argument("--limit", type=int, default=20)
    quality = commands.add_parser("coverage", help="Report evidence coverage of an investigation")
    quality.add_argument("case_id")
    quality.add_argument("--view", choices=["historical", "all"], default="historical")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    try:
        engine = ResearchRetrievalEngine(ResearchStore(args.root))
        if args.command == "search":
            filters = {key: value for key, value in {
                "case_id": args.case_id, "source_id": args.source_id,
                "publisher": args.publisher, "domain": args.domain,
                "case_kind": args.case_kind}.items() if value is not None}
            result = engine.search(args.query, kinds=args.kinds, filters=filters,
                                   limit=args.limit)
        elif args.command == "reconstruct":
            result = engine.reconstruct(args.case_id, view=args.view, cutoff=args.cutoff)
        elif args.command == "trace":
            result = engine.trace_question(args.case_id, args.question_id,
                                           view=args.view, max_depth=args.depth)
        elif args.command == "questions":
            result = engine.question_analysis(args.case_id, view=args.view)
        elif args.command == "question-convergence":
            result = engine.question_convergence(view=args.view,
                                                 minimum_cases=args.min_cases,
                                                 limit=args.limit)
        elif args.command == "compare-questions":
            result = engine.compare_questions(args.case_ids, view=args.view)
        elif args.command == "related":
            result = engine.related_cases(args.case_id, limit=args.limit)
        elif args.command == "coverage":
            pack = engine.reconstruct(args.case_id, view=args.view)
            result = {"case_id": args.case_id, "coverage": pack["coverage"],
                      "trajectory_gaps": pack["trajectory_gaps"],
                      "warnings": pack["warnings"]}
        else:
            parser.error("Unsupported command")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"research_engine: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
