import re
from datetime import datetime

from src.facade import DAYS, FORMAT_INTERVALS, PERIODS, FORMAT_LINES


def get_fee_day(interval: str) -> float:
    """
    From one string value, calculate the fee to pay for the functionary.
    :param interval: A str that comes splitted from the input.
                    Ex.: 'MO10:00-12:00'
    :return: A float number that depicts the fee to receive by
            the functionary in that day.
                    Ex.: 142.75
    """
    day, start_time, end_time = parse_interval(interval)
    return calc_fee_day(day, start_time, end_time)


def calc_fee_day(day: str, start_time: str, end_time: str) -> float:
    """
    Calculate the fee for one day, giving a start time and end time of work.
    :param day: A str of the day. Ex.: 'SA'
    :param start_time: A str that depicts the start work time. Ex.: '08:33'
    :param end_time: A str that depicts the end work time. Ex.: '17:47'
    :return: A double number. Ex.: 142.75
    """
    total_minutes = minutes_in_periods(start_time, end_time)
    fee_day = 0
    try:
        cost_min = [x / 60 for x in DAYS[day]['cost_hour'].values()]
        fee_day = round(sum(x * y for x, y in zip(cost_min, total_minutes)), 2)
    except KeyError as k:
        print(f'{k} is not a valid day.')
    return fee_day


def times_are_valid(times: list[str]) -> bool:
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


def parse_interval(interval: str) -> tuple[str, str, str]:
    """
    Split the interval in three elements. They are, start time of the working day,
    end time of the working day, and the abbreviation of the day.
    :param interval: A str that depicts the day, start time and end time
                    in one string. Ex.: 'SA14:00-18:00'
    :return: A tuple with three strings. Ex.: ('SA', '14:00', '18:00')
    """
    interval_parsed = interval.split('-')
    day = interval_parsed[0][:2]  # SU
    initial_hour = interval_parsed[0][2:]  # '19:00'
    end_hour = interval_parsed[1]  # '21:00'
    return day, initial_hour, end_hour


def minutes_in_periods(start_time: str, end_time: str) -> list[int, int, int]:
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
                minutes[i] = minutes_in_interval(start_time, end_time)
                break
            else:
                minutes[i] = minutes_in_interval(start_time, end_period)
        elif time_in_range(start_period, end_period, end_time):
            minutes[i] = minutes_in_interval(start_period, end_time)
        elif minutes[i - 1] != 0:
            try:
                if minutes[i + 1] is not None:
                    minutes[i] = minutes_in_interval(start_period, end_period)
            except IndexError:
                pass

    return minutes


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


def minutes_in_interval(start_time: str, end_time: str) -> int:
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


def read_data_person(data_person: str) -> str:
    """
    Process information of a functionary and inform how much have to be paid.
    :param data_person: A string with name and intervals read from the txt file.
                        Ex.: 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
    :return: A string communicating the mount to pay.
                        Ex.: The amount to pay ASTRID is: 85 USD'
    """

    if not validate_line(data_person):
        return 'Invalid format'
    info_days, name = parse_line(data_person)
    mount_for_person = sum(
        get_fee_day(info_day)
        for info_day in info_days
        if validate_interval(info_day)
    )

    return f"The amount to pay {name} is: {int(mount_for_person)} USD"


def validate_line(line: str) -> bool:
    """
    Validate if a line read from the file respect the pattern.
    :param line: A str read from the txt file.
            Ex.: 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    :return: True or False
    """
    return bool(re.match(FORMAT_LINES['regex'], line))


def parse_line(fileline: str) -> tuple[list[str], str]:
    """
    Split the information of a string in order to detect the name and the intervals.
    :param fileline: A string with the information of a functionary.
                    Ex:. 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
    :return: A tuple. Ex.: (['MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'], 'ASTRID')
    """
    parsed_string = fileline.split('=')
    name = parsed_string[0]
    info_days = parsed_string[1].split(',')
    return info_days, name


def read_file(path: str) -> list[str]:
    """
    Read a txt file that contains lines where every one are
    information of a functionary.
    :param path: Absolute path of the file.
                Ex.: r"C:\\Users\Alfonso\PycharmProjects\calc-payment\file.txt"
    :return: A List with the lines of the file.
    """
    try:
        with open(path) as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print('O Arquivo não existe')
