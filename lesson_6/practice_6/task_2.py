
"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения
данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить
метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""

#
# class Asphalt:
#
#     thickness: int
#     mass: int
#
#     def __init__(self, ):


class Road:

    __length: int
    __width: int

    def __init__(self, length: int, width: int):

        self.__length, self.__width = length, width

    def get_mass(self, mass_value: int, thickness_value: int) -> int:
        """

        :param thickness_value:
        :param mass_value:
        :return:
        """

        return self.__length * self.__width * mass_value * thickness_value


if __name__ == '__main__':

    while True:
        params = input('Введите через пробел значения асфальтового покрытия: '
                       'длина , ширина, масса и толщина: ').split(' ')
        for itm in params:
            if not itm.isdigit():
                print('Некорректные параметры! Вводить можно только числа.')
                params = None
                break
        if params is not None:
            rd = Road(length=int(params[0]), width=int(params[1]))
            print(f'{rd.get_mass(mass_value=int(params[2]), thickness_value=int(params[3]))}')
            break

    rd = Road(length=20, width=5000)
    assert rd.get_mass(25, 5) == 12500000, 'Ошибка!'

