
"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
from os import path

if __name__ == '__main__':

    file_name = 'file.txt'
    try:
        with open(file_name, 'r', encoding='UTF-8') as f_obj:
            lis = f_obj.read().splitlines()
            print(f'Количество строк в файле: {len(lis)}')
            for itm in enumerate(lis, 1):
                print(f'Кол-во строк в строке № {itm[0]}: {0 if itm[1].strip() == "" else len(itm[1].split(" "))}')
    except FileNotFoundError:
        print(f'Файл не найден {path.join(path.dirname(__file__), file_name)}')
    except Exception as ex:
        print(f'Произошла ошибка ввода/вывода({str(ex)}).')
