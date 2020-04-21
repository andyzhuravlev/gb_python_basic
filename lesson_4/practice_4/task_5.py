
"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from random import uniform as uniform
from functools import reduce as reduce


def get_list() -> list:
    """

    :return:
    """

    return [i for i in range(100, 1001) if i % 2 == 0]


if __name__ == '__main__':

    lis = get_list()
    print(reduce(lambda x, y: x * y, lis))
