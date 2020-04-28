
"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.
"""


class Stationery:

    title: str

    def __init__(self, title: str):

        title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self):

        super().__init__(title='Ручка')

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):

    def __init__(self):
        super().__init__(title='Карандаш')

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):

    def __init__(self):
        super().__init__(title='Маркер')

    def draw(self):
        print('Рисуем маркером')


if __name__ == '__main__':

    st1 = Pen()
    st1.draw()

    st2 = Pencil()
    st2.draw()

    st3 = Handle()
    st3.draw()