import pytest

from src.tools import time_in_range


@pytest.fixture
def start_time():
    return '18:00'


@pytest.fixture
def end_time():
    return '19:01'


@pytest.fixture
def looked_time_18_30():
    return '18:30'


def test_18_30_in_between_18_00__19_01(start_time, end_time, looked_time_18_30):
    assert time_in_range(start_time, end_time, looked_time_18_30)


@pytest.fixture
def looked_time_19_30():
    return '19:30'


def test_19_30_not_in_between_18_00__19_00(start_time, end_time, looked_time_19_30):
    assert time_in_range(start_time, end_time, looked_time_19_30) is False
