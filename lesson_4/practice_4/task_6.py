
"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import count as count
from itertools import cycle as cycle
from my_gen import get_list as get_list


def iter_1(start: int):
    """

    :param start:
    :return:
    """

    for i in count(start):
        print(i)


def iter_2(lis: list):
    """

    :return:
    """

    for itm in cycle(lis):
        print(itm)


if __name__ == '__main__':

    print(f'[0] - бесконечный итератор, генерирующий целые числа, начиная с указанного.\n'
          f'[1] - бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.')

    value = input('Выберите необходимый пункт: ')
    if value.isdigit():
        value = int(value)
        if value == 0:
            value = input('Введите нижний предел для генерации: ')
            if value.isdigit():
                iter_1(int(value))
            else:
                print('Это не число!')
        elif value == 1:
            lis = get_list(0, 10, 20)
            iter_2(lis)
        else:
            print('Вариант не реализован!')
    else:
        print('Вариант не реализован!')
