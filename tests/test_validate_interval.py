from src.validators import validate_interval


def test_MO_01_00_14_00_is_valid():
    assert validate_interval('MO01:00-14:00')


def test_MON_01_00_14_00_invalid_day():
    assert validate_interval('M0N1:00-14:00') is False


def test_SU_81_00_14_00__one_invalid_time():
    assert validate_interval('SU81:00-14:00') is False


def test_FR_01_91_14_85__two_invalid_time():
    assert validate_interval('FR01:91-14:85') is False


def test_MO_01_00_14_00_day_and_times_are_invalid():
    assert validate_interval('M1:00-4:00') is False


def test_return_boolean():
    assert isinstance(validate_interval('MO01:00-14:00'), bool)
