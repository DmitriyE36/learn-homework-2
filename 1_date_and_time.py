"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")

def print_days():
    d_now = datetime.now().date()
    delta1 = timedelta(days=1)
    delta2 = timedelta(days=30)
    print(f'Вчера: {d_now - delta1}')
    print(f'Сегодня: {d_now}')
    print(f'30 дней назад: {d_now - delta2}')


def str_2_datetime(date_string):
    dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
