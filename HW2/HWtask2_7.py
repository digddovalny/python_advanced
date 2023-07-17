'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''

value: int = int(input("Введите целое число для преобразования: "))
HEX_NUMBER: int = 16
dictionary = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}


def converter_to_hex(val: int):
    result: str = ""
    while val > 0:
        temp_value = str(val % HEX_NUMBER)
        result_value = dictionary.get(temp_value,temp_value)
        result += result_value
        val //= HEX_NUMBER
    correct_result = "".join(reversed(result))
    return correct_result


value_in_hex_sys = converter_to_hex(value)
print(f"число {value} в шестнадцатеричной системе равно будет выглядеть так --> {value_in_hex_sys}")
print(f"Число в шестнадцатеричной системе при помощи hex --> {hex(value)}")
