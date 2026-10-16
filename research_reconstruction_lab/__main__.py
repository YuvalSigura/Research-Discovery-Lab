"""Read-only CLI for a provisional evidence-centered research reconstruction."""
import argparse
import json
import sys
from pathlib import Path
from . import inspect, PackError


def main(argv=None):
    p = argparse.ArgumentParser(prog="python -m research_reconstruction_lab")
    p.add_argument("pack", type=Path, help="JSON file with evidence and competing interpretations")
    a = p.parse_args(argv)
    try:
        result = inspect(json.loads(a.pack.read_text(encoding="utf-8")))
    except (OSError, ValueError, PackError) as exc:
        print(json.dumps({"status": "invalid_pack", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
