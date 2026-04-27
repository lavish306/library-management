from datetime import datetime


def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%d-%m-%Y")
    except ValueError:
        return None


def days_between(date1, date2):
    return (date2 - date1).days


def get_date_input(prompt):
    while True:
        val = input(prompt).strip()
        d = parse_date(val)
        if d:
            return d
        print("Wrong format. Enter date as DD-MM-YYYY")
