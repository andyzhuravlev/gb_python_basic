
"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

from os import path

if __name__ == '__main__':

    file_name = 'emp.txt'
    try:
        with open(file_name, 'r', encoding='UTF-8') as f_obj:
            a = 1
    except FileNotFoundError:
        print(f'Файл не найден {path.join(path.dirname(__file__), file_name)}')
    except Exception as ex:
        print(f'Произошла ошибка ввода/вывода({str(ex)}).')
