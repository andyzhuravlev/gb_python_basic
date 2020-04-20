
"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def calculate_salary(params: list) -> int:
    """

    :param params:
    :return:
    """
    salary = 0
    if len(params) == 4:
        cont = True
        for itm in sys.argv[1:]:
            if not itm.isdigit():
                cont = False
                break
        if cont:
            salary = int(params[1]) * int(params[2]) + int(params[3])
        else:
            print(f'Некорректные параметры команды!({itm})')
    else:
        print('Неверное количество параметров!')

    return salary


if __name__ == '__main__':
    # print(f'{calculate_salary(["task_1.py", 1000, 1200, 2000])}')
    print(f'{calculate_salary(sys.argv)}')
