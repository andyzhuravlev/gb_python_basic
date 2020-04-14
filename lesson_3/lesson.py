# функции
# my_list = [1, 1, 2, 3, 3, 3]
# try:
#     a = my_list[10] / 0
# except ZeroDivisionError:
#     print('Деление на ноль')
# except IndexError:
#     print('Не хорошо')
# except Exception:
#     print('Все ошибки')
# finally:
#     print('Выполнится в любом случае')

# define - определение
# def my_test(a, b):
#     return a + b
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = map(*2, my_list)
#
# a = my_test(2, 3)
# print(a)


def my_sum(a, b, c: int = 22):
    return a + b + c


tmp = my_sum(1, 2, 3)
print(tmp)