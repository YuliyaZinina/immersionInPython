"""
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
"""

BASE: int = 16
BASE_ALPHABET = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

num: int = int(input('Введите целое число: '))
print(hex(num))


def decimal_to_number_system (number: int, base=BASE, base_alphabet=BASE_ALPHABET) -> str:
    result: str = ''
    result_list: list[str] = []

    while number > 0:
        result_list.append(BASE_ALPHABET[number % BASE])
        number = number // BASE

    while result_list:
        result += result_list.pop()

    return result


print('With base=', BASE, 'result=', decimal_to_number_system(num))
