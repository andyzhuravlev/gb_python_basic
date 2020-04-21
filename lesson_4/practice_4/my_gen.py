
from random import uniform as uniform


def get_list(start: int, stop: int, limit: int) -> list:
    """
    :param start: нижняя граница для генерации размера списка
    :param stop: верхняя граница для генерации размера списка
    :param limit: верхняя граница для генерации значения элемента списка
    :return:
    """
    size_of_list = int(uniform(start, stop))

    return [int(uniform(i, limit)) for i in range(0, size_of_list)]