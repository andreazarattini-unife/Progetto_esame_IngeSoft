"""Command line interface for automated ZMTransform executions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from zmtransform.analysis import analyze_directory_to_workbook


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def run(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.input_dir, args.output_file)


if __name__ == "__main__":
    raise SystemExit(main())
