from src.tools import minutes_in_periods


def test_16_00__18_00_return_0_120_0__worked_one_period():
    assert minutes_in_periods('16:00', '18:00') == [0, 120, 0]


def test_16_00__18_25_return_0_120_24__worked_two_periods():
    assert minutes_in_periods('16:00', '18:25') == [0, 120, 24]


def test_07_10__12_25_return_110_204_0_worked_two_periods():
    assert minutes_in_periods('07:10', '12:25') == [110, 204, 0]


def test_08_33__18_25_return_27_539_24__worked_all_periods():
    assert minutes_in_periods('08:33', '18:25') == [27, 539, 24]


def test_19_33__21_25_return_0_0_112__worked_one_period():
    assert minutes_in_periods('19:33', '21:25') == [0, 0, 112]


def test_00_15__09_00_return_525_0_0__worked_one_period():
    assert minutes_in_periods('00:15', '09:00') == [525, 0, 0]


def test_00_05__23_10_return_525_0_0__worked_all_periods():
    assert minutes_in_periods('00:15', '23:00') == [525, 539, 299]


def test_return_is_list():
    assert isinstance(minutes_in_periods('00:15', '09:00'), list)
