from users_module import user_input


def function_1(var_1: int, var_2: int) -> float:
    """
    функция выполняет деление на 0 и возвращает результат,
    в случае деления на 0 возвращает None
    :param var_1: делимое
    :param var_2: делитель
    :return:
    """
    res = None
    try:
        res = var_1 / var_2
    except ZeroDivisionError:
        print('Деление на 0!')

    return res


print(function_1(user_input('a'), user_input('b')))