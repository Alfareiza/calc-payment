from src.tools import read_data_person


def test_name_and_intervals_filled():
    assert read_data_person('RENE=MO10:00-12:00,TU10:00-12:00,'
                            'TH01:00-03:00,SA14:00-18:00,'
                            'SU20:00-21:00') == 'The amount to pay RENE is: 215 USD'


def test_long_name_and_filled_intervals():
    assert read_data_person('EZEQUIEL=MO10:00-12:00,TH12:00-14:00,'
                            'SU20:00-21:00') == 'The amount to pay EZEQUIEL is: 85 USD'


def test_name_and_some_empty_intervals():
    assert read_data_person('ALFONSO=MO08:00-17:00,FRI9:15-18:05,,'
                            'SA17:35-18:55') == 'The amount to pay ALFONSO is: 175 USD'


def test_filled_name_and_all_intervals_emtpy():
    assert read_data_person('JAN=,,,,,') == 'The amount to pay JAN is: 0 USD'


def test_empty_name_and_all_intervals_emtpy():
    assert read_data_person('=,,,,,') == 'Invalid format'
