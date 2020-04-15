
# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

from users_module import user_input


def my_pow(x: int, y: int) -> int:
    """
    функция возведения в степень
    :param x:
    :param y:
    :return:
    """
    # res = 1
    # for i in range(1, y if y > 0 else -y):
    #     res *= x
    # if y < 0:
    #     res = 1 / res

    return x ** y


print(my_pow(user_input('x'), - user_input('y')))
