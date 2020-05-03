
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):

    result_code_desctiption: str = 'Деление на 0!!'


class Calc:

    @staticmethod
    def div(x: int, y: int) -> float:
        """

        :param x:
        :param y:
        :return:
        """

        result = 0
        try:
            result = x / y
        except ZeroDivisionError:
            raise MyZeroDivisionError

        return result


if __name__ == '__main__':

    while True:
        x = 153315
        y = input(f'Делимое - {x}, введите делитель : ')
        if not y.isdecimal():
            print('Это не число!')
            continue

        try:
            print(f'Результат деления: {Calc.div(x, int(y))}')
        except MyZeroDivisionError as ex:
            print(ex.result_code_desctiption)

