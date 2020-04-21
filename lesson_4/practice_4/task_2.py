
"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

from random import uniform as uniform
from my_gen import get_list as get_list


if __name__ == '__main__':

    lis = get_list(20, 30, 100)
    i = 0
    print(lis)
    while i < len(lis):
        tmp = [itm for itm in lis[i:] if itm > lis[i]]
        if len(tmp):
            print(tmp)
        i += 1



