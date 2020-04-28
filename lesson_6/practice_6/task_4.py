
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

from time import sleep

class Car:

    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed: int, color: str, name: str, is_police: bool = False):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """

        :return:
        """
        print(f'Машина поехала {self.name} {self.color}')

    def stop(self):
        """

        :return:
        """
        print('Машина остановилась')

    def turn(self, direction: str):
        """

        :param direction:
        :return:
        """
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'{self.speed}')


class TownCar(Car):

    def __init__(self, speed: int, color: str, name: str):

        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            Car.show_speed(self)


class SportCar(Car):

    def __init__(self, speed: int, color: str, name: str):

        super().__init__(speed, color, name)


class WorkCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            Car.show_speed()


class PoliceCar(Car):

    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name, True)


if __name__ == "__main__":

    tc = TownCar(40, 'Черный', 'Хундай солярис')
    tc.go()

    tc.show_speed()

    tc.turn('направо')
    tc.turn('направо')
    tc.turn('налево')

    tc.speed = 100
    tc.show_speed()

    tc.stop()

    sleep(2)
    print('')

    sc = SportCar(60, 'Красный', 'Порше 911')
    sc.go()

    sc.show_speed()

    sc.turn('налево')
    sc.turn('налево')

    sc.speed = 250
    sc.show_speed()

    sc.stop()

