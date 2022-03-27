from datetime import datetime
import re

from src.facade import FORMAT_INTERVALS, DAYS, FORMAT_LINES
from typing import List

def times_are_valid(times: List[str]) -> bool:
    """
    Verify if times are valid (both of them).
    If at least one of them is invalid, will return False.
    A time is valid when respect the pattern HH:MM and is on 24hrs format.
    :param times: A list with start time and end time.
                    Ex.: ['10:15','20:02']
    :return: True or False
    """
    valid_dates = False
    for time in times:
        try:
            datetime.strptime(time, '%H:%M')
            valid_dates = True
        except ValueError:
            valid_dates = False
            break
    return valid_dates


def validate_interval(interval: str) -> bool:
    """
    Validates if the interval meets the conditions of the established format.
    :param interval: A str that depicts the day, start time and end time in one
                    string. Ex.: 'MO01:00-14:00'
    :return: True or False
    """
    if re.match(FORMAT_INTERVALS['regex'], interval):
        day, times = interval[:2], interval[2:].split('-')
        return bool(day in DAYS.keys() and times_are_valid(times))
    else:
        return False


def validate_line(line: str) -> bool:
    """
    Validate if a line read from the file respect the pattern.
    :param line: A str read from the txt file.
            Ex.: 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    :return: True or False
    """
    return bool(re.match(FORMAT_LINES['regex'], line))


def time_in_range(start_time: str, end_time: str, looked_time: str) -> bool:
    """
    Validate if looked_time is within start_time and end_time.
    :param start_time: A str that depicts the start time. Ex.: '18:00'
    :param end_time: A str that depicts the end time. Ex.: '19:01'
    :param looked_time: A str that depicts the looked time. Ex.: '18:30'
    :return: True or False
    """
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    looked_time = datetime.strptime(looked_time, '%H:%M')
    if start_time <= end_time:
        return start_time <= looked_time <= end_time
    else:
        return start_time <= looked_time or looked_time <= end_time
