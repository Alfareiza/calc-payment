from src.calculators import calc_minutes_in_interval


def test_120_minutes_between_10_00__12_00():
    assert calc_minutes_in_interval('10:00', '12:00') == 120


def test_145_minutes_between_09_51__12_16():
    assert calc_minutes_in_interval('09:51', '12:16') == 145


def test_return_integer():
    assert isinstance(calc_minutes_in_interval('09:51', '12:16'), int)
