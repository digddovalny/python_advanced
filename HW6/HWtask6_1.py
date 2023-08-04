# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

def if_leap(year: int):
    return not (year%4 != 0 or year%100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    day, mounth, year = map(int, str_date.split('.'))
    if not (1 < day < 31 and 1 < mounth< 12 and 1 < year < 9999):
        return False
    if mounth in (4, 6, 9, 11) and day > 30:
        return False
    if mounth == 2 and if_leap(year) and day > 29:
        return False
    if mounth == 2 and not if_leap(year) and day > 28:
        return False
    return True

if __name__ == '__main__':
    name, *date = argv
    print(check_date(*(int(elem) for elem in date)))