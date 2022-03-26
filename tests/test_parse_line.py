from src.tools import parse_line


def test_parse_line_name_and_intervals_filled():
    assert parse_line('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00') == (
        ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00'], 'ASTRID')


def test_parse_line_with_some_empty_intervals():
    assert parse_line('ASTRID=MO10:00-12:00,,SU20:00-21:00') == (['MO10:00-12:00', '', 'SU20:00-21:00'], 'ASTRID')


def test_parse_line_with_all_empty_intervals():
    assert parse_line('ASTRID=,,,') == (['', '', '', ''], 'ASTRID')
