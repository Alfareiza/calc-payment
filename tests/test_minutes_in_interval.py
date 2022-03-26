from src.tools import minutes_in_interval


def test_120_minutes_between_10_00__12_00():
    assert minutes_in_interval('10:00', '12:00') == 120


def test_145_minutes_between_09_51__12_16():
    assert minutes_in_interval('09:51', '12:16') == 145


def test_return_integer():
    assert isinstance(minutes_in_interval('09:51', '12:16'), int)
