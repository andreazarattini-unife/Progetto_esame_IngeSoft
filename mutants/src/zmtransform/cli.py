"""Command line interface for automated ZMTransform executions."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated

from zmtransform.analysis import analyze_directory_to_workbook

mutants_x_build_parser__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_parser__mutmut)
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


def x_build_parser__mutmut_orig() -> argparse.ArgumentParser:
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


def x_build_parser__mutmut_1() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = None
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


def x_build_parser__mutmut_2() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog=None,
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


def x_build_parser__mutmut_3() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description=None,
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


def x_build_parser__mutmut_4() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
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


def x_build_parser__mutmut_5() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
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


def x_build_parser__mutmut_6() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="XXzmtransformXX",
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


def x_build_parser__mutmut_7() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="ZMTRANSFORM",
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


def x_build_parser__mutmut_8() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="XXAnalizza cartelle BS/TS e genera il file Excel riepilogativo.XX",
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


def x_build_parser__mutmut_9() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="analizza cartelle bs/ts e genera il file excel riepilogativo.",
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


def x_build_parser__mutmut_10() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="ANALIZZA CARTELLE BS/TS E GENERA IL FILE EXCEL RIEPILOGATIVO.",
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


def x_build_parser__mutmut_11() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        None,
        type=Path,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_12() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=None,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_13() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help=None,
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_14() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        type=Path,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_15() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_16() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_17() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "XXinput_dirXX",
        type=Path,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_18() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "INPUT_DIR",
        type=Path,
        help="Cartella contenente le sottocartelle BS e TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_19() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="XXCartella contenente le sottocartelle BS e TS.XX",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_20() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="cartella contenente le sottocartelle bs e ts.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_21() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="zmtransform",
        description="Analizza cartelle BS/TS e genera il file Excel riepilogativo.",
    )
    parser.add_argument(
        "input_dir",
        type=Path,
        help="CARTELLA CONTENENTE LE SOTTOCARTELLE BS E TS.",
    )
    parser.add_argument(
        "output_file",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_22() -> argparse.ArgumentParser:
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
        None,
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_23() -> argparse.ArgumentParser:
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
        type=None,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_24() -> argparse.ArgumentParser:
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
        help=None,
    )
    return parser


def x_build_parser__mutmut_25() -> argparse.ArgumentParser:
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
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_26() -> argparse.ArgumentParser:
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
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_27() -> argparse.ArgumentParser:
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
        )
    return parser


def x_build_parser__mutmut_28() -> argparse.ArgumentParser:
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
        "XXoutput_fileXX",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_29() -> argparse.ArgumentParser:
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
        "OUTPUT_FILE",
        type=Path,
        help="Percorso del file Excel da generare.",
    )
    return parser


def x_build_parser__mutmut_30() -> argparse.ArgumentParser:
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
        help="XXPercorso del file Excel da generare.XX",
    )
    return parser


def x_build_parser__mutmut_31() -> argparse.ArgumentParser:
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
        help="percorso del file excel da generare.",
    )
    return parser


def x_build_parser__mutmut_32() -> argparse.ArgumentParser:
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
        help="PERCORSO DEL FILE EXCEL DA GENERARE.",
    )
    return parser

mutants_x_build_parser__mutmut['_mutmut_orig'] = x_build_parser__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_1'] = x_build_parser__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_2'] = x_build_parser__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_3'] = x_build_parser__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_4'] = x_build_parser__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_5'] = x_build_parser__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_6'] = x_build_parser__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_7'] = x_build_parser__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_8'] = x_build_parser__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_9'] = x_build_parser__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_10'] = x_build_parser__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_11'] = x_build_parser__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_12'] = x_build_parser__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_13'] = x_build_parser__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_14'] = x_build_parser__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_15'] = x_build_parser__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_16'] = x_build_parser__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_17'] = x_build_parser__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_18'] = x_build_parser__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_19'] = x_build_parser__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_20'] = x_build_parser__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_21'] = x_build_parser__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_22'] = x_build_parser__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_23'] = x_build_parser__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_24'] = x_build_parser__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_25'] = x_build_parser__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_26'] = x_build_parser__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_27'] = x_build_parser__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_28'] = x_build_parser__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_29'] = x_build_parser__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_30'] = x_build_parser__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_31'] = x_build_parser__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_parser__mutmut['x_build_parser__mutmut_32'] = x_build_parser__mutmut_32 # type: ignore # mutmut generated
mutants_x_run__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_run__mutmut)
def run(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_orig(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_1(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = None
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_2(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(None)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_3(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=None, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_4(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=None)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_5(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_6(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, )
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_7(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=False, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_8(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=False)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_9(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(None)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_10(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(None, file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_11(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=None)

    return 1 if errors else 0


def x_run__mutmut_12(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(file=sys.stderr)

    return 1 if errors else 0


def x_run__mutmut_13(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, )

    return 1 if errors else 0


def x_run__mutmut_14(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 2 if errors else 0


def x_run__mutmut_15(input_dir: Path, output_file: Path) -> int:
    """Run the batch analysis and save the result workbook."""
    workbook, errors = analyze_directory_to_workbook(input_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output_file)

    for error in errors:
        print(error, file=sys.stderr)

    return 1 if errors else 1

mutants_x_run__mutmut['_mutmut_orig'] = x_run__mutmut_orig # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_1'] = x_run__mutmut_1 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_2'] = x_run__mutmut_2 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_3'] = x_run__mutmut_3 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_4'] = x_run__mutmut_4 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_5'] = x_run__mutmut_5 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_6'] = x_run__mutmut_6 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_7'] = x_run__mutmut_7 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_8'] = x_run__mutmut_8 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_9'] = x_run__mutmut_9 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_10'] = x_run__mutmut_10 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_11'] = x_run__mutmut_11 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_12'] = x_run__mutmut_12 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_13'] = x_run__mutmut_13 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_14'] = x_run__mutmut_14 # type: ignore # mutmut generated
mutants_x_run__mutmut['x_run__mutmut_15'] = x_run__mutmut_15 # type: ignore # mutmut generated
mutants_x_main__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_main__mutmut)
def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.input_dir, args.output_file)


def x_main__mutmut_orig(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.input_dir, args.output_file)


def x_main__mutmut_1(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = None
    return run(args.input_dir, args.output_file)


def x_main__mutmut_2(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(None)
    return run(args.input_dir, args.output_file)


def x_main__mutmut_3(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(None, args.output_file)


def x_main__mutmut_4(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.input_dir, None)


def x_main__mutmut_5(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.output_file)


def x_main__mutmut_6(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = build_parser().parse_args(argv)
    return run(args.input_dir, )

mutants_x_main__mutmut['_mutmut_orig'] = x_main__mutmut_orig # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_1'] = x_main__mutmut_1 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_2'] = x_main__mutmut_2 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_3'] = x_main__mutmut_3 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_4'] = x_main__mutmut_4 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_5'] = x_main__mutmut_5 # type: ignore # mutmut generated
mutants_x_main__mutmut['x_main__mutmut_6'] = x_main__mutmut_6 # type: ignore # mutmut generated


if __name__ == "__main__":
    raise SystemExit(main())
