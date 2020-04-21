
"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

from random import uniform as uniform


def get_list() -> list:
    """

    :return:
    """

    size_of_list = int(uniform(40, 50))

    return [int(uniform(i, 30)) for i in range(0, size_of_list)]


if __name__ == '__main__':

    lis = get_list()
    print(lis)
    print([itm for itm in lis if lis[lis.index(itm) + 1:].count(itm) == 0])
