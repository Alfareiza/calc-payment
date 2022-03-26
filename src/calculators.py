from datetime import datetime

from src.facade import DAYS, PERIODS
from src.validators import time_in_range


def calc_fee_day(day: str, start_time: str, end_time: str) -> float:
    """
    Calculate the fee for one day, giving a start time and end time of work.
    :param day: A str of the day. Ex.: 'SA'
    :param start_time: A str that depicts the start work time. Ex.: '08:33'
    :param end_time: A str that depicts the end work time. Ex.: '17:47'
    :return: A double number. Ex.: 142.75
    """
    total_minutes = calc_minutes_in_periods(start_time, end_time)
    fee_day = 0
    try:
        cost_min = [x / 60 for x in DAYS[day]['cost_hour'].values()]
        fee_day = round(sum(x * y for x, y in zip(cost_min, total_minutes)), 2)
    except KeyError as k:
        print(f'{k} is not a valid day.')
    return fee_day


def calc_minutes_in_periods(start_time: str, end_time: str) -> list[int, int, int]:
    """
    Calculate how many minutes the functionary worked and return a list
     where every index depicts the minutes in that period.
    :param start_time: A str that depicts the start time. Ex.: '08:30'
    :param end_time: A str that depicts the start time '08:30'. Ex.: '17:22'
    :return: A list with 3 integers. Ex.: [0, 530, 0]
    """
    minutes = [0] * len(PERIODS.values())
    for i, period in enumerate(PERIODS.values()):
        start_period, end_period = [x.strip() for x in period.split('-')]
        if time_in_range(start_period, end_period, start_time):
            if time_in_range(start_period, end_period, end_time):
                minutes[i] = calc_minutes_in_interval(start_time, end_time)
                break
            else:
                minutes[i] = calc_minutes_in_interval(start_time, end_period)
        elif time_in_range(start_period, end_period, end_time):
            minutes[i] = calc_minutes_in_interval(start_period, end_time)
        elif minutes[i - 1] != 0:
            try:
                if minutes[i + 1] is not None:
                    minutes[i] = calc_minutes_in_interval(start_period, end_period)
            except IndexError:
                pass

    return minutes


def calc_minutes_in_interval(start_time: str, end_time: str) -> int:
    """
    Calculate the minutes in a given interval of time.
    :param start_time: A str that depicts the time that started
                        to work. Ex.: '10:00'
    :param end_time: A str that depicts the time that started to work.
                        Ex.: '12:00'
    :return: An integer. Ex.: 120
    """
    tdelta = datetime.strptime(end_time, '%H:%M') - datetime.strptime(start_time, '%H:%M')
    return int(round(tdelta.total_seconds() / 60, 1))