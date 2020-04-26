
"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

from time import sleep


class Color:

    def __init__(self, color: str, sleep_time: int):

        self.color = color
        self.sleep_time = sleep_time


class TrafficLight:

    def __init__(self, color: int = 0):

        self._color: int = 0

    def running(self):

        colors = [
            Color(color='\033[41m', sleep_time=7),
            Color(color='\033[43m', sleep_time=2),
            Color(color='\033[42m', sleep_time=8),
        ]

        i = 0
        while True:
            print(colors[self._color].color)
            sleep(colors[self._color].sleep_time)
            self._color += 1
            if self._color == 2:
                self._color, colors = 0, colors[-1::-1]


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
