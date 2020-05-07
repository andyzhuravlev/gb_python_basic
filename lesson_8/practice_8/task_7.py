"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:

    r: int
    i: int

    def __init__(self, re: int, im: int):
        self.r = re
        self.i = im

    def sum(self, z2: object):
        pass

    def mlt(self: object, z2: object):
        pass


class Z(Complex):

    def __init__(self, re: int, im: int):
        self.r = re
        self.i = im

    def sum(self, z2: Complex) -> Complex:
        return Complex(re=self.r + z2.r, im=self.i + z2.i)

    def mlt(self, z2: Complex):
        return Complex(re=self.r * z2.r - self.i * z2.i, im=self.r * z2.i + self.i * z2.r)


if __name__ == '__main__':
    z1 = Z(2, 5)
    z2 = Complex(4, -2)
    complex_sum = z1.sum(z2)
    print(f'(2, 5) + (4, -2) = ({complex_sum.r}, {complex_sum.i})')
    complex_mlt = z1.mlt(z2)
    print(f'(2, 5) * (4, -2) = ({complex_mlt.r}, {complex_mlt.i})')


