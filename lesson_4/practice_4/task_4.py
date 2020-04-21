
"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

from random import uniform as uniform
from my_gen import get_list as get_list


if __name__ == '__main__':

    lis = get_list(40, 50, 30)
    print(lis)
    print([itm for itm in lis if lis[lis.index(itm) + 1:].count(itm) == 0])
