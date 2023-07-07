# immersionInPython
Home works for GB course

## [Home work 1](https://github.com/YuliyaZinina/immersionInPython/tree/main/homeWork1)
1. [task1Triangle.py](https://github.com/YuliyaZinina/immersionInPython/blob/main/homeWork1/task1Triangle.py)
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

2. [task2IsSimpleNumber.py](https://github.com/YuliyaZinina/immersionInPython/blob/main/homeWork1/task2IsSimpleNumber.py)
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

3. [task3GuessTheNumber.py](https://github.com/YuliyaZinina/immersionInPython/blob/main/homeWork1/task3GuessTheNumber.py)
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
