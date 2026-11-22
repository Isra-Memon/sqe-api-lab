import pytest
from src.percentile import percentile


def test_percentile_lowest_student():
    assert percentile(10, [10, 20, 30]) == 0.0


def test_percentile_highest_student():
    assert percentile(30, [10, 20, 30]) == 100.0


def test_percentile_middle_student():
    assert percentile(20, [10, 20, 30]) == 50.0


def test_percentile_single_student_roster():
    assert percentile(50, [50]) == 100.0


def test_percentile_empty_roster_raises():
    with pytest.raises(ValueError):
        percentile(50, [])


def test_percentile_student_not_in_roster_raises():
    with pytest.raises(ValueError):
        percentile(99, [10, 20, 30])