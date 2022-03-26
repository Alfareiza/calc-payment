from src.validators import validate_line


def test_name_and_intervals_filled():
    assert validate_line(
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')


def test_long_name_and_filled_intervals():
    assert validate_line(
        'EZEQUIEL=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00')


def test_name_and_some_empty_intervals():
    assert validate_line(
        'ALFONSO=MO08:00-17:00,FRI9:15-18:05,,SA17:35-18:55')


def test_filled_name_and_all_intervals_emtpy():
    assert validate_line('JAN=,,,,,')


def test_empty_name_and_all_intervals_emtpy():
    assert validate_line('=,,,,,') is False
