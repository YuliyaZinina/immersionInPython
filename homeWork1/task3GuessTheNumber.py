"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

count = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
number = randint(LOWER_LIMIT, UPPER_LIMIT)
print(number)

while count > 0:
    print('Осталось ', count, 'попыток')
    count -= 1
    print('Введите целое число от ', LOWER_LIMIT, ' до ', UPPER_LIMIT, ': ')
    inputNumber = int(input())
    if inputNumber < number:
        print('Больше')
    elif inputNumber > number:
        print('Меньше')
    else:
        print('Угадал! Поздравляю!')
        break
else:
    print('Ты исчерпал все попытки. Повезёт в другой раз!')
