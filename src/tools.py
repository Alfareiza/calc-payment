from src.calculators import calc_fee_day
from src.facade import DAYS
from src.parsers import parse_interval, parse_line
from src.validators import validate_interval, validate_line


def get_fee_day(interval: str) -> tuple[float, str]:
    """
    From one string value, calculate the fee to pay for the functionary.
    :param interval: A str that comes splitted from the input.
                    Ex.: 'MO10:00-12:00'
    :return: A float number that depicts the fee to receive by
            the functionary in that day.
                    Ex.: 142.75
    """
    day, start_time, end_time = parse_interval(interval)
    return calc_fee_day(day, start_time, end_time), DAYS[day]['name']


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
    intervals, name = parse_line(data_person)
    print(f'\n{name} ↓')
    mount_person = 0
    for interval in intervals:
        if validate_interval(interval):
            mount_day, day = get_fee_day(interval)
            mount_person += mount_day
            print(f'\tPayment of : {mount_day} on {day}')
        else:
            print(f'\tInvalid date/time format -> \"{interval}\"')

    return f"The amount to pay {name} is: {int(mount_person)} USD"


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


def main(path: str):
    """
    Main file of the program who read the file and start to execute all the intelligence
    :param path: Absolute path of the file.
                Ex.: r"C:\\Users\Alfonso\PycharmProjects\calc-payment\file.txt"
    :return: Nothing
    """
    try:
        lines = read_file(path)
        print(f'Reading information from the file \"{path}\"')
        for line in lines:
            print(read_data_person(line.strip()))
        print('\n\nThanks by using our software !!')
    except TypeError:
        print(f'Verify that the file exists in the folder')
