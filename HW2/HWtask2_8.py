'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''

from fractions import Fraction

first_fraction: str = input("Введите первую дробь: ")
second_fraction: str = input("Введите вторую дробь: ")

numerator_first_fraction, denominator_first_fraction = first_fraction.split('/')
numerator_second_fraction, denominator_second_fraction = second_fraction.split('/')


def calculate_NOK(val_denom_first: int, val_denom_second: int):
    if val_denom_first > val_denom_second:
        main = val_denom_first
    else:
        main = val_denom_second
    while (True):
        if (main % val_denom_first == 0) and (main % val_denom_second == 0):
            result_NOK = main
            break
        main += 1
    return result_NOK


def calculate_NOD(val_denom_first: int, val_denom_second: int):
    if val_denom_first > val_denom_second:
        smaller = val_denom_second
    else:
        smaller = val_denom_first
    for i in range(1, smaller + 1):
        if (val_denom_first % i == 0) and (val_denom_second % i == 0):
            nod = i
    return nod


def sum_fractions(num_fisrt: int, denom_first: int, num_second: int, denom_second: int):
    if int(denom_first) == int(denom_second):
        result = f"{int(num_fisrt) + int(num_second)}/{denom_first}"
        return result
    else:
        NOK = calculate_NOK(int(denom_first), int(denom_second))
        result = f"{int(numerator_first_fraction) * (int(NOK / int(denominator_first_fraction))) + int(numerator_second_fraction) * (int(NOK / int(denominator_second_fraction)))}/{NOK}"
        return result


def transformation_fractions(numerator: int, denominator: int):
    nod = calculate_NOD(int(numerator), int(denominator))
    if int(numerator) == (denominator):
        return "1"
    else:
        result_numerator: int = int(int(numerator) / nod)
        result_denominator: int = int(int(denominator) / nod)
        result_fraction = f"{result_numerator}/{result_denominator}"
        return result_fraction


def multiply_fractions(num_fisrt: int, denom_first: int, num_second: int, denom_second: int):
    result = f"{int(num_fisrt) * int(num_second)}/{int(denom_first) * int(denom_second)}"
    return result


if int(denominator_first_fraction) == 0 or int(denominator_second_fraction) == 0:
    print("Ошибка!!! На ноль делить нельзя")
else:
    numerator_for_summ, denominator_for_summ = (
        sum_fractions(numerator_first_fraction, denominator_first_fraction, numerator_second_fraction,
                      denominator_second_fraction)).split('/')
    numerator_for_multy, denominator_for_multy = (
        multiply_fractions(numerator_first_fraction, denominator_first_fraction, numerator_second_fraction,
                           denominator_second_fraction)).split('/')
    res_sum = transformation_fractions(int(numerator_for_summ), int(denominator_for_summ))
    res_multy = transformation_fractions(int(numerator_for_multy), int(denominator_for_multy))

    print(f"Сумма дробей равна: {res_sum}")
    print(f"Cумма по fractions: {Fraction(3, 15) + Fraction(4, 18)}")
    print(f"Перемножение дробей равно: {res_multy}")
    print(f"Перемножение по fractions: {Fraction(3, 15) * Fraction(4, 18)}")
