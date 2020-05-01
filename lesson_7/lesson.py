
from abc import ABC, abstractmethod
import  time
# понятие абстрактного класса


class MyInterface(ABC):

    @abstractmethod
    def turn_on(self, x: int, y: int) -> float:
        pass

    @abstractmethod
    def turn_off(self, x: int) -> None:
        pass


class MyClass(MyInterface):

    def __init__(self):
        self.one = '222222'

    def turn_on(self, x: int, y: int) -> float:
        pass

    def turn_off(self, x: int) -> None:
        pass

# декораторы


def my_deco(func):
    def wrap():
        print(func.__name__)
        func()
        return func()

    return  wrap()


@my_deco
def test1():
    print('test 1')


@my_deco
def test2():
    print('test 2')


if __name__ == '__main__':

    tmp = MyClass()

