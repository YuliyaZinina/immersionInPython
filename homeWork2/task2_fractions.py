"""
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions.

"""

from fractions import Fraction

fraction1: str = '2/5'
fraction2: str = '4/5'

a = Fraction(fraction1)
b = Fraction(fraction2)
print('check sum=', a + b)
print('check mult', a * b)


def get_numerator(fraction: str) -> int:
    numerator: int = int(fraction.split('/')[0])
    return numerator


def get_denominator(fraction: str) -> int:
    denominator: int = int(fraction.split('/')[1])
    return denominator


def get_fractions_sum(fraction_a: str, fraction_b: str) -> str:
    result: str = ''
    denominator_a: int = get_denominator(fraction_a)
    denominator_b: int = get_denominator(fraction_b)
    numerator_a: int = get_numerator(fraction_a)
    numerator_b: int = get_numerator(fraction_b)

    if denominator_a == denominator_b:
        denominator_res = denominator_a
    else:
        denominator_res = denominator_a * denominator_b
        numerator_a *= denominator_b
        numerator_b *= denominator_a

    numerator_res = numerator_a + numerator_b
    result = result + str(numerator_res) + '/' + str(denominator_res)

    return result


def get_fractions_mult(fraction_a: str, fraction_b: str) -> str:
    result: str = ''
    denominator_a: int = get_denominator(fraction_a)
    denominator_b: int = get_denominator(fraction_b)
    numerator_a: int = get_numerator(fraction_a)
    numerator_b: int = get_numerator(fraction_b)

    numerator_res = numerator_a * numerator_b
    denominator_res = denominator_a * denominator_b

    result = result + str(numerator_res) + '/' + str(denominator_res)

    return result


print('Sum =', get_fractions_sum(fraction1, fraction2))
print('Mult =', get_fractions_mult(fraction1, fraction2))

