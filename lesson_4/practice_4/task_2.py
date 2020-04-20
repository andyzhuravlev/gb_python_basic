
"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

from random import uniform as uniform


def get_list() -> list:
    """

    :return:
    """

    size_of_list = int(uniform(20, 30))

    return [int(uniform(i, 100)) for i in range(0, size_of_list)]


if __name__ == '__main__':

    lis = get_list()
    i = 0
    print(lis)
    while i < len(lis):
        tmp = [itm for itm in lis[i:] if itm > lis[i]]
        if len(tmp):
            print(tmp)
        i += 1



