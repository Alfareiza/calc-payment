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
