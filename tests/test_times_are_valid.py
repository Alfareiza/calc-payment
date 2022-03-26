from src.validators import times_are_valid


def test_10_15__20_02_are_valid():
    assert times_are_valid(['10:15', '20:02'])


def test_70_15__20_02__at_least_one_is_invalid():
    assert times_are_valid(['70:15', '20:02']) is False


def test_10_15__25_02__at_least_one_is_invalid():
    assert times_are_valid(['10:15', '25:02']) is False


def test_70_15__25_02_are_invalid():
    assert times_are_valid(['70:15', '25:02']) is False


def test_receive_more_than_one_parameter():
    assert times_are_valid(['10:15', '15:02', '12:15'])


def test_receive_empty_list_return_false():
    assert times_are_valid([]) is False


def test_return_boolean():
    assert isinstance(times_are_valid(['70:15', '25:02']), bool)
