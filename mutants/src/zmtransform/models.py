"""Domain models used by the zinc measurement analysis."""

# pylint: disable=too-many-instance-attributes

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ProfileStatistics:
    """Descriptive statistics calculated from a measurement profile."""

    average: float
    standard_deviation: float
    minimum: float
    maximum: float


#Composizione dei dati per lato (campi uguali per BS e TS)
@dataclass(frozen=True)
class MeasurementSummary:
    """Statistical summary extracted from one measurement workbook."""

    coil_id: Any
    date_time: Any
    nominal: Any
    total_length: Any
    average: float
    standard_deviation: float
    minimum: float
    maximum: float
    source_file: Path


@dataclass(frozen=True)
class AnalysisRow:
    """Result row composed by one BS measurement and its optional TS match."""

    bs: MeasurementSummary
    ts: MeasurementSummary | None
