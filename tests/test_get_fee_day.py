from src.tools import get_fee_day


def test__MO10_00_12_00__return_30_0_Monday():
    assert get_fee_day('MO10:00-12:00') == (30.0, 'Monday')


def test__TU10_00_12_00__return_30_0_Tuesday():
    assert get_fee_day('TU10:00-12:00') == (30.0, 'Tuesday')


def test__TH01_00_03_00__return_50_0_Thursday():
    assert get_fee_day('TH01:00-03:00') == (50.0, 'Thursday')


def test__SA08_00_18_00__return_09_67_Saturday():
    assert get_fee_day('SA08:00-18:00') == (209.67, 'Saturday')


def test__SU20_00_21_00__return_25_0_Sunday():
    assert get_fee_day('SU20:00-21:00') == (25.0, 'Sunday')


def test__TH12_00_14_00__return_30_0_Thursday():
    assert get_fee_day('TH12:00-14:00') == (30.0, 'Thursday')


def test__SU17_00_19_00__return_44_58_Sunday():
    assert get_fee_day('SU17:00-19:00') == (44.58, 'Sunday')
