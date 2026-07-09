"""Unit tests for the analysis module."""

# pylint: disable=missing-function-docstring

import math

import openpyxl
import pytest
from hypothesis import given
from hypothesis import strategies as st

from zmtransform.analysis import (
    MeasurementFileError,
    calculate_statistics,
    create_result_workbook,
    read_measurement_file,
    read_profile_values,
)
from zmtransform.models import AnalysisRow


@pytest.mark.unit
def test_read_measurement_file_calculates_summary(tmp_path, workbook_factory):
    workbook_path = tmp_path / "coil.xlsx"
    workbook_factory(workbook_path, measurements=[10.0, 20.0, 30.0])

    summary = read_measurement_file(workbook_path)

    assert summary.coil_id == "COIL-001"
    assert summary.nominal == 120.0
    assert summary.total_length == 3
    assert summary.average == 20.0
    assert summary.minimum == 10.0
    assert summary.maximum == 30.0
    assert summary.standard_deviation == pytest.approx(10.0)


@pytest.mark.unit
def test_read_measurement_file_rejects_missing_sheet(tmp_path, workbook_factory):
    workbook_path = tmp_path / "invalid.xlsx"
    workbook_factory(workbook_path)

    workbook = openpyxl.load_workbook(workbook_path)
    del workbook["LengthProfiles"]
    workbook.save(workbook_path)

    with pytest.raises(MeasurementFileError, match="LengthProfiles"):
        read_measurement_file(workbook_path)


@pytest.mark.unit
def test_read_profile_values_does_not_depend_on_max_row(tmp_path, workbook_factory):
    workbook_path = tmp_path / "coil.xlsx"
    workbook_factory(workbook_path, measurements=[10.0, 20.0, 30.0])
    workbook = openpyxl.load_workbook(workbook_path, read_only=True, data_only=True)
    sheet = workbook["LengthProfiles"]

    total_length, measurements = read_profile_values(sheet, workbook_path)

    assert total_length == 3
    assert measurements == [10.0, 20.0, 30.0]


@pytest.mark.unit
def test_create_result_workbook_writes_bs_and_ts_columns(tmp_path, workbook_factory):
    bs_path = tmp_path / "bs.xlsx"
    ts_path = tmp_path / "ts.xlsx"
    workbook_factory(bs_path, measurements=[10.0, 20.0, 30.0])
    workbook_factory(ts_path, measurements=[40.0, 50.0, 60.0])
    bs_summary = read_measurement_file(bs_path)
    ts_summary = read_measurement_file(ts_path)

    workbook = create_result_workbook([AnalysisRow(bs=bs_summary, ts=ts_summary)])
    sheet = workbook["Dati"]

    assert sheet["A1"].value == "CoilID"
    assert sheet["A2"].value == "COIL-001"
    assert sheet["E2"].value == 20.0
    assert sheet["K2"].value == 50.0


@pytest.mark.unit
@given(
    st.lists(
        st.floats(min_value=-10_000, max_value=10_000, allow_nan=False, allow_infinity=False),
        min_size=2,
        max_size=50,
    )
)
def test_calculate_statistics_property(values):
    stats = calculate_statistics(values)

    assert stats.minimum == min(values)
    assert stats.maximum == max(values)
    assert stats.minimum <= stats.average or math.isclose(stats.minimum, stats.average)
    assert stats.average <= stats.maximum or math.isclose(stats.average, stats.maximum)
    assert stats.standard_deviation >= 0
    assert math.isfinite(stats.average)
    assert math.isfinite(stats.standard_deviation)
