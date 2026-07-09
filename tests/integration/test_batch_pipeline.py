"""Integration tests for the batch analysis pipeline."""

# pylint: disable=missing-function-docstring

import openpyxl
import pytest

from zmtransform.analysis import analyze_directory_to_workbook, find_input_files
from zmtransform.cli import main, run


@pytest.mark.integration
def test_analyze_directory_to_workbook_matches_bs_and_ts(tmp_path, workbook_factory):
    input_dir = tmp_path / "input"
    workbook_factory(
        input_dir / "BS" / "coil_001.xlsx",
        coil_id="COIL-001",
        measurements=[100.0, 110.0, 120.0],
    )
    workbook_factory(
        input_dir / "TS" / "coil_001.xlsx",
        coil_id="COIL-001",
        measurements=[90.0, 95.0, 100.0],
    )

    bs_files, ts_files = find_input_files(input_dir)
    workbook, errors = analyze_directory_to_workbook(input_dir)
    sheet = workbook["Dati"]

    assert len(bs_files) == 1
    assert len(ts_files) == 1
    assert not errors
    assert sheet["A2"].value == "COIL-001"
    assert sheet["E2"].value == 110.0
    assert sheet["K2"].value == 95.0


@pytest.mark.integration
def test_cli_writes_output_workbook(tmp_path, workbook_factory):
    input_dir = tmp_path / "input"
    output_file = tmp_path / "out" / "result.xlsx"
    workbook_factory(
        input_dir / "BS" / "coil_001.xlsx",
        coil_id="COIL-001",
        measurements=[1.0, 2.0, 3.0],
    )
    workbook_factory(
        input_dir / "TS" / "coil_001.xlsx",
        coil_id="COIL-001",
        measurements=[4.0, 5.0, 6.0],
    )

    exit_code = run(input_dir, output_file)

    assert exit_code == 0
    assert output_file.exists()
    workbook = openpyxl.load_workbook(output_file)
    assert workbook["Dati"]["A2"].value == "COIL-001"
    assert workbook["Dati"]["E2"].value == 2.0
    assert workbook["Dati"]["K2"].value == 5.0


@pytest.mark.integration
def test_cli_main_parses_arguments_and_writes_output(tmp_path, workbook_factory):
    input_dir = tmp_path / "input"
    output_file = tmp_path / "out" / "result.xlsx"
    workbook_factory(
        input_dir / "BS" / "coil_001.xlsx",
        coil_id="COIL-001",
        measurements=[7.0, 8.0, 9.0],
    )

    exit_code = main([str(input_dir), str(output_file)])

    assert exit_code == 0
    assert output_file.exists()
