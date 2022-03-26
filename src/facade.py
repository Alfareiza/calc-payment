EXPLANATION = """
            This program calculate the fee of a employee trough information comes from a txt file according to the next pattern:
            \t\t\t\t\t\"JANE=MO10:00-12:00,WE08:15-17:51,SU20:00-21:00\"
            Then, will be printed on the screen the salary of every employee. Be sure that there is a txt file on the folder.
            """

FORMAT_INTERVALS = {
    'regex': '^[A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2}$',
    'example': 'JANE=MO10:00-12:00,WE08:15-17:51,SU20:00-21:00',
}
FORMAT_LINES = {
    'regex': '^[A-Z]+=[A-Z0-9\-:,]+',
    'example': 'MO11:37-20:02',
}
PERIODS = {
    'period_one': '00:01 - 09:00',
    'period_two': '09:01 - 18:00',
    'period_three': '18:01 - 00:00'
}
WEEKDAYS = {
    PERIODS['period_one']: 25,
    PERIODS['period_two']: 15,
    PERIODS['period_three']: 20
}
WEEKEND = {
    PERIODS['period_one']: 30,
    PERIODS['period_two']: 20,
    PERIODS['period_three']: 25
}
DAYS = {
    'MO': {'name': 'Monday', 'cost_hour': WEEKDAYS},
    'TU': {'name': 'Tuesday', 'cost_hour': WEEKDAYS},
    'WE': {'name': 'Wednesday', 'cost_hour': WEEKDAYS},
    'TH': {'name': 'Thursday', 'cost_hour': WEEKDAYS},
    'FR': {'name': 'Friday', 'cost_hour': WEEKDAYS},
    'SA': {'name': 'Saturday', 'cost_hour': WEEKEND},
    'SU': {'name': 'Sunday', 'cost_hour': WEEKEND}
}
