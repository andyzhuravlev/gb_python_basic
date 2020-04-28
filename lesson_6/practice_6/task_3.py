"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать
данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    _income: dict

    def __init__(self, name: str, surname: str, position: str, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position

        self._income = {
            'wage': 50000,
            'bonus': 20000,
        }


class Position(Worker):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        return f'{self.name.title()} {self.surname.title()}'

    def get_total_income(self) -> int:
        return sum(self._income.values())


if __name__ == '__main__':

    while True:
        lis = input('Введите через пробел данные о работнике "имя фамилия должность": ').split(' ')
        if len(lis) == 3:
            pos = Position(name=lis[0], surname=lis[1], position=lis[2])
            assert pos.get_full_name() == f'{lis[0].title()} {lis[1].title()}', 'Ошибка в представлениии полного имени'
            assert pos.get_total_income() == 70000, 'Ошибка расчета дохода'
            print(f'Все хорошо')
            break
        else:
            print('Неверное количество аргументов!')
