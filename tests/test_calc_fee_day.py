from src.calculators import calc_fee_day


def test_weekday_same_period():
    assert calc_fee_day('MO', '10:00', '12:00') == 30.0


def test_weekday_differents_periods_one_next_to_other():
    assert calc_fee_day('WE', '16:00', '18:25') == 38.0


def test_weekday_differents_periods_one_distant_to_other():
    assert calc_fee_day('FR', '07:00', '21:00') == 244.42


def test_weekend_same_period():
    assert calc_fee_day('SA', '10:00', '12:00') == 40.0


def test_weekend_differents_periods_one_next_to_other():
    assert calc_fee_day('SU', '16:00', '18:25') == 50.0


def test_weekend_differents_periods_one_distant_to_other():
    assert calc_fee_day('SA', '07:00', '21:00') == 314.25


def test_weekday_invalid_day():
    assert calc_fee_day('FRI', '10:00', '12:00') == 0
