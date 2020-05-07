
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    __date: str = ''
    mm: str
    dd: str
    yy: str

    def __init__(self, date: str):

        self.__date = date
        self.mm = '1'
        self.dd = '1'
        self.yy = '2017'

    @classmethod
    def get_date(cls):

        return cls.__date

    @staticmethod
    def validate() -> bool:

        return True


if __name__ == '__main__':

    date = Date(input('Введите дату в формате dd-mm-yyyy: '))
    temp = Date.get_date()
    a = 1
