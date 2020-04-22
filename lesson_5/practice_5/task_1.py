
"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

from os import path as path

if __name__ == '__main__':

    file_name = path.join(path.dirname(__file__), 'user_input.txt')
    print(f'Записываем файл {file_name}')
    with open(file_name, 'w', encoding='UTF-8') as f_obj:
        while True:
            input_string = input(f'Введите строку для записи в файл {file_name}: ')
            if input_string.strip() == '':
                break
            print(input_string, file=f_obj)
