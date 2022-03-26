from src.parsers import parse_interval


def test_valid_format():
    assert parse_interval('SA14:00-18:00') == ('SA', '14:00', '18:00')
