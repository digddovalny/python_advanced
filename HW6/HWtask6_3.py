# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


import random
from HW6.HWtask6_2 import check_chess


def generate_positions():
    position_x = list(range(1, 9))
    position_y = list(range(1, 9))
    COUNT = 8
    for i in range(4):  # 4 успешные расстановки
        random.shuffle(position_x)
        random.shuffle(position_y)
        while not check_chess(position_x, position_y, COUNT):
            random.shuffle(position_x)
            random.shuffle(position_y)
        print(f"позиции х: {position_x}\t позиции у: {position_y}")

generate_positions()