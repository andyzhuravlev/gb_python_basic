
def user_input(name: str) -> int:
    """
    функция запрашивает значение переменной и возвращает его
    :param name: имя переменной
    :param positive: ввод положительного числа или отрицательного
    :return:
    """
    while True:
        result_str = input(f'Введите число {name}: ')
        if not result_str.isdigit():
            print('Это не число!')
            continue
        return int(result_str)
