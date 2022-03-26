import os
import pathlib

from src.facade import EXPLANATION
from src.tools import read_data_person, read_file

FOLDER = pathlib.Path(__file__).parent.resolve()


def main(path: str):
    try:
        lines = read_file(path)
        print(f'Reading information from the file \"{path}\"')
        for line in lines:
            print(read_data_person(line.strip()))
        print('\n\nThanks by using our software !!')
    except TypeError:
        print(f'Verify that the file exists in the folder {FOLDER}\\')


def ask():
    txt_files = [file for file in os.listdir(FOLDER) if file.endswith(".txt") and not file.startswith('requirements')]
    if not txt_files:
        print(f'Please, place a txt file on the folder {FOLDER}\\ and then execute the program again.\n')
    else:
        start = input('Should I start to calculate the information (S/N): ')
        if start.upper() == 'S':
            main(txt_files[0])
        elif start.upper() == 'N':
            print('Thanks by using our software')
        else:
            print('Invalid Information')
            ask()


if __name__ == '__main__':
    print(EXPLANATION)
    ask()
