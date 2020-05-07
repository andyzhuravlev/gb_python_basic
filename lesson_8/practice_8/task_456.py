"""
на вебинарах все вроде понятно
моей большой ошибкой было не закреплять материал после занятий в течение ближайшего времени
в текущей задаче возникло много проблем в связи с этим, поздно приступил к ней
реализация не очень, ООП буду персматривать

1. заполняем справочник склады
2. заполняем справочник номенклатура
3. вводим приходную накладную
4. вводим внетреннее перемещение по остаткам на складе
"""

import json
from abc import ABC, abstractmethod, abstractproperty
from os import path
from datetime import datetime
from random import randint


class AppSettings:
    """
    класс для работы с параметрами приложения
    опеределение кталога хранения файлов базы данных
    опеределение имен файлов базы данных
    """

    __path = path.dirname(__file__)
    __unit_file_name = path.join(__path, 'unit')
    __storage_file_name = path.join(__path, 'storage')
    __goods_file_name = path.join(__path, 'goods')
    __purchase_invoice_file_name = path.join(__path, 'purchase_invoice')
    __goods_stocks_file_name = path.join(__path, 'goods_stocks')
    __inner_invoice_file_name = path.join(__path, 'inner_invoice')

    __file_mode = 'a+'
    __file_encoding = 'utf-8'

    @classmethod
    def unit_file_name(cls):
        return cls.__unit_file_name

    @classmethod
    def storage_file_name(cls):
        return cls.__storage_file_name

    @classmethod
    def goods_file_name(cls):
        return cls.__goods_file_name

    @classmethod
    def file_mode(cls):
        return cls.__file_mode

    @classmethod
    def file_encoding(cls):
        return cls.__file_encoding

    @classmethod
    def purchase_invoice_file_name(cls):
        return cls.__purchase_invoice_file_name

    @classmethod
    def goods_stocks_file_name(cls):
        return cls.__goods_stocks_file_name

    @classmethod
    def inner_invoice_file_name(cls):
        return cls.__inner_invoice_file_name


class DataAdapter:
    """
    класс для работы с базой данных
    """

    @staticmethod
    def get_goods() -> list:
        """
        загрузка продуктов из базы данных
        :return: словарь с продуктами
        """
        result = []
        try:
            with open(AppSettings.goods_file_name(), 'r',
                      encoding=AppSettings.file_encoding()) as f_obj:
                for line in f_obj:
                    result.append(json.loads(line))
        except FileNotFoundError as ex:
            """ файл не найден, возвращаем пустой список """
        return result

    @staticmethod
    def save_goods(product_description_json: str) -> bool:
        """
        сохранение в базе элемента справочника продукты
        :param product_description_json:
        :return:
        """
        with open(AppSettings.goods_file_name(), 'a',
                  encoding=AppSettings.file_encoding()) as f_obj:
            f_obj.write(product_description_json + '\n')
        return True

    @staticmethod
    def get_storage() -> list:
        """
        загрузка справочника склады из базы данных
        :return:
        """
        result = []
        try:
            with open(AppSettings.storage_file_name(), 'r',
                      encoding=AppSettings.file_encoding()) as f_obj:
                for line in f_obj:
                    result.append(json.loads(line))
        except FileNotFoundError as ex:
            """ файл не найден, возвращаем пустой список """
        return result

    @staticmethod
    def save_storage(storage_description_json: str) -> bool:
        """
        сохранение в базе элемента справочника склады
        :param storage_description_json:
        :return:
        """
        with open(AppSettings.storage_file_name(), 'a',
                  encoding=AppSettings.file_encoding()) as f_obj:
            f_obj.write(storage_description_json + '\n')
        return True

    @staticmethod
    def save_purchase_invoice(invoice_description_json: str) -> bool:
        """
        сохранение в базе приходной накладной
        :param invoice_description_json:
        :return:
        """
        with open(AppSettings.purchase_invoice_file_name(), 'a',
                  encoding=AppSettings.file_encoding()) as f_obj:
            f_obj.write(invoice_description_json + '\n')
        return True

    @staticmethod
    def update_goods_stocks(record_set: list) -> bool:
        """
        сохранение в базе запасов номенклатуры
        :param record_set:
        :return:
        """
        with open(AppSettings.goods_stocks_file_name(), 'a',
                  encoding=AppSettings.file_encoding()) as f_obj:
            for record in record_set:
                f_obj.write(json.dumps(record) + '\n')
        return True

    @staticmethod
    def get_goods_stocks_by_storage(id_storage: int) -> list:
        """
        получение из базы данных запасов номенклатуры по конкретному складу
        :param id_storage:
        :return:
        """
        result = []
        try:
            with open(AppSettings.goods_stocks_file_name(), 'r',
                      encoding=AppSettings.file_encoding()) as f_obj:
                for line in f_obj:
                    current_record = json.loads(line)
                    if current_record['id_storage'] == id_storage:
                        result.append(current_record)
        except FileNotFoundError as ex:
            """ файл не найден, возвращаем пустой список """
        return result

    @staticmethod
    def save_inner_invoice(invoice_description_json: str) -> bool:
        """
        сохранение в базе данных внутреннего перемещения
        :param invoice_description_json:
        :return:
        """
        with open(AppSettings.inner_invoice_file_name(), 'a',
                  encoding=AppSettings.file_encoding()) as f_obj:
            f_obj.write(invoice_description_json + '\n')
        return True


class Unit:

    __id_len: int = 5
    __name_len: int = 30
    __id: int
    __name: str

    def __init__(self, name: str):
        self.name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @id.setter
    def name(self, new_name: str):
        self.__name = new_name

    @staticmethod
    def validate_name_len(new_name: str) -> bool:
        """
        проверка длины имени
        :param new_name:
        :return:
        """
        return len(new_name) <= Unit.__name_len

    @staticmethod
    def load_units(data_json: str):
        """
        инициализация списка единиц измерения, загружаем из данных файла __
        :param data_json:
        :return:
        """
        with open(AppSettings.unit_file_name, 'b+', encoding='utf-8') as unit_file_obj:
            for itm in json.loads(unit_file_obj.read()):
                i = 0


class Storage:

    __name_len = 100
    __id: int
    __name: str

    def __init__(self, name: str):
        self.__name = name
        self.__id = randint(1, 10000000)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @staticmethod
    def validate_name_len(new_name: str) -> bool:
        """
        проерка длины имени
        :param new_name:
        :return:
        """
        return len(new_name) <= Storage.__name_len

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'name': self.__name,
            'id': self.__id,
        })


class Goods:
    """
    базовый класс номенклатура
    """

    __id: int
    __kind: int
    name: str
    color: str
    manufacturer: str

    @abstractmethod
    def get_json(self):
        pass

    @staticmethod
    def get_goods_by_id(id_goods: int, goods_list: list) -> dict:
        """
        получение элемента справочника номенклатура по идентификатору
        :param id_goods:
        :param goods_list:
        :return:
        """
        result = None
        for itm in goods_list:
            if itm['id'] == id_goods:
                result = itm
        return result


class Printer(Goods):

    def __init__(self, name: str, color: str, manufacturer: str, print_speed: int, rom: int):
        """

        :param name: наименование принтера
        :param color: цвет принтера
        :param manufacturer: производитель
        :param print_speed: скорость печати
        :param rom: встроенная память в МБ
        """
        self.name = name
        self.color = color
        self.manufacturer = manufacturer
        self.print_speed = print_speed
        self.rom = rom
        self.__kind = 0
        self.__id = randint(1, 2000000000)

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'name': self.name,
            'color': self.color,
            'manufacturer': self.manufacturer,
            'print_speed': self.print_speed,
            'rom': self.rom,
            'kind': self.__kind,
            'id': self.__id,
        })


class Scanner(Goods):

    def __init__(self, name: str, color: str, manufacturer: str, scan_speed: int, color_scan: bool = True):
        """

        :param name: наименование сканера
        :param color: цвет сканера
        :param manufacturer: производитель
        :param scan_speed: скорость сканирования в секундах
        :param color_scan: цветное сканирование
        """
        self.name = name
        self.color = color
        self.manufacturer = manufacturer
        self.scan_speed = scan_speed
        self.color_scan = color_scan
        self.__kind = 1
        self.__id = randint(2000000000, 4000000000)

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'name': self.name,
            'color': self.color,
            'manufacturer': self.manufacturer,
            'scan_speed': self.scan_speed,
            'color_scan': self.color_scan,
            'kind': self.__kind,
            'id': self.__id,
        })


class Xerox(Goods):

    def __init__(self, name: str, color: str, manufacturer: str, copy_speed: int, weight: int,
                 can_scan: bool = True, can_print: bool = True):
        """

        :param name: наименование МФУ
        :param color: цвет
        :param manufacturer: производитель
        :param copy_speed: скорость копирования в секундах
        :param weight: вес
        :param can_scan: есть сканер
        :param can_print: есть принтер
        """
        self.name = name
        self.color = color
        self.manufacturer = manufacturer
        self.copy_speed = copy_speed
        self.weight = weight
        self.can_scan = can_scan
        self.can_print = can_print
        self.__kind = 2
        self.__id = randint(4000000000, 6000000000)

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'name': self.name,
            'color': self.color,
            'manufacturer': self.manufacturer,
            'copy_speed': self.copy_speed,
            'weight': self.weight,
            'can_scan': self.can_scan,
            'can_print': self.can_print,
            'kind': self.__kind,
            'id': self.__id,
        })


@abstractmethod
class Invoice:
    """
    базовый класс накладная
    """

    @property
    def id(self): int
    invoice_date: datetime
    goods: list
    comment: str
    id_storage: int

    def get_json(self):
        pass


class PurchaseInvoice(Invoice):
    """
    приходная накладная
    """

    __id: int

    def __init__(self, id_storage: int, comment: str = ''):
        self.__id = randint(1, 4000000000)
        self.invoice_date = datetime.now()
        self.id_storage = id_storage
        self.comment = comment
        self.goods = []

    @property
    def id(self):
        return self.__id

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'invoice_date': self.invoice_date.strftime("%Y-%m-%d-%H.%M.%S"),
            'id_storage': self.id_storage,
            'comment': self.comment,
            'goods': self.goods,
            'id': self.__id,
        })


class InnerInvoice(Invoice):
    """
    у внутренней накладной нужно добавить еще склад назначения
    пока класс просто скопирован
    """
    __id: int

    def __init__(self, id_storage: int, comment: str = ''):
        self.__id = randint(1, 4000000000)
        self.invoice_date = datetime.now()
        self.id_storage = id_storage
        self.comment = comment
        self.goods = []

    @property
    def id(self):
        return self.__id

    def get_json(self) -> str:
        """
        сериализация класса
        :return: строка json
        """
        return json.dumps({
            'invoice_date': self.invoice_date.strftime("%Y-%m-%d-%H.%M.%S"),
            'id_storage': self.id_storage,
            'comment': self.comment,
            'goods': self.goods,
            'id': self.__id,
        })


class GoodsStocks:
    """
    класс для остатков номенклатуры
    """

    id_storage: int
    id_goods: int
    count: int
    price: int

    def __init__(self, id_storage: int, id_goods: int, count: int, price: int):
        self.id_storage = id_storage
        self.id_goods = id_goods
        self.count = count
        self.price = price


class UserUIX:
    """
    класс для работы с пользовтельским вводом
    """

    @staticmethod
    def print_main_menu():
        """
        прорисовка основного меню(супервизор)
        :return:
        """
        print('[1] - Справочник номеклатура')
        print('[2] - Справочник склады')
        print('[3] - Прием номенклатуры на склад')
        print('[4] - Внутреннее перемещение')
        print('[0] - Выход')

    @staticmethod
    def print_incorrect_input():
        """
        вывод ошибки
        :return:
        """
        print('Некорректный ввод!')

    @staticmethod
    def add_new_printer():
        """
        ввод пользователем нового принтера
        :return:
        """
        print('Введите через пробел свойства принтера')
        user_input = input('"наименование" "цвет" "производитель" '
                           '"скорость печати" "объем встроенной пямяти в МБ": ')
        user_input = user_input.split(' ')
        if len(user_input) != 5:
            print('Неверное количество свойств!')
        else:
            new_printer = Printer(name=user_input[0], color=user_input[1], manufacturer=user_input[2],
                                  print_speed=user_input[3], rom=user_input[4])
            while True:
                user_input = input('Добавить новый принтер в базу данных? 0 - нет, 1 - да: ')
                if not user_input.isdigit():
                    UserUIX.print_incorrect_input()
                    continue

                user_input = int(user_input)
                if user_input == 1:
                    DataAdapter.save_goods(new_printer.get_json())
                break

    @staticmethod
    def add_new_scanner():
        """
        ввод пользователем нового сканера
        :return:
        """
        print('Введите через пробел свойства сканера')
        user_input = input('"наименование" "цвет" "производитель" "скорость сканирования" "цветная печать": ')
        user_input = user_input.split(' ')
        if len(user_input) != 5:
            print('Неверное количество свойств!')
        else:
            new_scaner = Scanner(name=user_input[0], color=user_input[1], manufacturer=user_input[2],
                                  scan_speed=user_input[3], color_scan=user_input[4])
            while True:
                user_input = input('Добавить новый сканер в базу данных? 0 - нет, 1 - да: ')
                if not user_input.isdigit():
                    UserUIX.print_incorrect_input()
                    continue

                user_input = int(user_input)
                if user_input == 1:
                    DataAdapter.save_goods(new_scaner.get_json())
                break

    @staticmethod
    def add_new_xerox():
        """
        ввод пользователем нового ксерокса
        :return:
        """
        print('Введите через пробел свойства ксерокса')
        user_input = input('"наименование" "цвет" "производитель" "скорость копирования в секундах" '
                           '"вес" "есть сканер" "есть принтер": ')
        user_input = user_input.split(' ')
        if len(user_input) != 7:
            print('Неверное количество свойств!')
        else:
            while True:
                new_xerox = Xerox(name=user_input[0], color=user_input[1], manufacturer=user_input[2],
                                  copy_speed=user_input[3], weight=user_input[4], can_scan=user_input[5],
                                  can_print=user_input[6])
                user_input = input('Добавить новый ксерокс в базу данных? 0 - нет, 1 - да: ')
                if not user_input.isdigit():
                    UserUIX.print_incorrect_input()
                    continue

                user_input = int(user_input)
                if user_input == 1:
                    DataAdapter.save_goods(new_xerox.get_json())
                break

    @staticmethod
    def add_new_storage():
        """
        ввод пользователем нового склада
        :return:
        """
        user_input = input('Введите наименование склада: ')
        new_storage = Storage(name=user_input)
        while True:
            user_input = input('Добавить новый склад в базу данных? 0 - нет, 1 - да: ')
            if not user_input.isdigit():
                UserUIX.print_incorrect_input()
                continue

            user_input = int(user_input)
            if user_input == 1:
                DataAdapter.save_storage(new_storage.get_json())
            break


if __name__ == '__main__':

    while True:
        UserUIX.print_main_menu()
        user_input = input('Выберите действие: ')
        if not user_input.isdigit():
            UserUIX.print_incorrect_input()
            continue

        user_input = int(user_input)
        if user_input == 0:
            break
        elif user_input == 1:
            while True:
                print('Справочник номенклатура')
                goods = DataAdapter.get_goods()
                for idx, itm in enumerate(goods, 1):
                    print(f'{idx} - {itm}')
                print('[1] - Добавить новую номенклатуру')
                print('[0] - Выход в предыдущее меню')
                user_input = input('Выберите действия для справочника номенклатура: ')
                if not user_input.isdigit():
                    UserUIX.print_incorrect_input()
                    continue

                user_input = int(user_input)
                if user_input == 0:
                    break
                elif user_input == 1:
                    while True:
                        print('1 - Принтер')
                        print('2 - Сканер')
                        print('3 - Ксерокс')
                        print('0 - Выход в предыдущее меню')
                        user_input = input('Выберите тип номенклатуры: ')
                        if not user_input.isdigit():
                            UserUIX.print_incorrect_input()
                            continue

                        user_input = int(user_input)
                        if user_input == 1:
                            UserUIX.add_new_printer()
                        elif user_input == 2:
                            UserUIX.add_new_scanner()
                        elif user_input ==3:
                            UserUIX.add_new_xerox()
                        elif user_input > 0:
                            UserUIX.print_incorrect_input()
                        else:
                            break
        elif user_input == 2:
            while True:
                print('Справочник складов')
                storage = DataAdapter.get_storage()
                for idx, itm in enumerate(storage, 1):
                    print(f'{idx} - {itm}')
                print('[1] - Добавить новый склад')
                print('[0] - Выход в предыдущее меню')
                user_input = input('Выберите действия для справочника склады: ')
                if not user_input.isdigit():
                    UserUIX.print_incorrect_input()
                    continue

                user_input = int(user_input)
                if user_input == 0:
                    break
                elif user_input == 1:
                    UserUIX.add_new_storage()
        elif user_input == 3:
            storage = DataAdapter.get_storage()
            if len(storage) == 0:
                print('Справочник складов пуст! Сначала необходимо добавить хотя бы один склад!')
            else:
                while True:
                    for idx, itm in enumerate(storage, 1):
                        print(f'{idx} - {itm}')
                    user_input = input('Выберите склад: ')
                    if not user_input.isdigit():
                        UserUIX.print_incorrect_input()
                        continue
                    user_input = int(user_input)
                    if user_input > len(storage):
                        UserUIX.print_incorrect_input()
                        continue
                    current_storage = storage[user_input - 1]
                    goods = DataAdapter.get_goods()
                    if len(goods) == 0:
                        print('Справочник номенклатуры пуст! Сначала необходимо добавить хотя бы одну номенклатуру!')
                    else:
                        current_goods = []
                        for idx, itm in enumerate(goods, 1):
                            print(f'{idx} - {itm}')
                        print('Для выхода введите 0')
                        while True:
                            user_input = input('Введите через пробел "порядковый номер номенклатуры"'
                                               ' "количество" "цена": ')
                            if user_input.isdigit():
                                if int(user_input) == 0:
                                    break
                            user_input = user_input.split(' ')
                            if len(user_input) != 3:
                                UserUIX.print_incorrect_input()
                                continue
                            if not user_input[1].isdigit() or not user_input[2].isdigit():
                                print('Некорректные параметры: количество или цена!')
                                continue
                            current_goods.append(
                                {
                                    'id_storage': current_storage['id'],
                                    'id_goods': goods[int(user_input[0]) - 1]['id'],
                                    'count': int(user_input[1]),
                                    'price': int(user_input[2])
                                }
                            )
                        if len(current_goods) > 0:
                            while True:
                                user_input = input('Сохранить прием номенклатуры? 0 - нет, 1 - да: ')
                                if not user_input.isdigit():
                                    UserUIX.print_incorrect_input()
                                    continue
                                user_input = int(user_input)
                                if user_input > 1:
                                    UserUIX.print_incorrect_input()
                                    continue
                                invoice = PurchaseInvoice(id_storage=current_storage['id'])
                                for itm in current_goods:
                                    invoice.goods.append(itm)
                                if DataAdapter.save_purchase_invoice(invoice.get_json()):
                                    DataAdapter.update_goods_stocks(current_goods)
                                break
                            break
        elif user_input == 4:
            storage = DataAdapter.get_storage()
            if len(storage) == 0:
                print('Справочник складов пуст! Сначала необходимо добавить хотя бы один склад!')
            else:
                goods = DataAdapter.get_goods()
                while True:
                    for idx, itm in enumerate(storage, 1):
                        print(f'{idx} - {itm}')
                    user_input = input('Выберите склад: ')
                    if not user_input.isdigit():
                        UserUIX.print_incorrect_input()
                        continue
                    user_input = int(user_input)
                    if user_input > len(storage):
                        UserUIX.print_incorrect_input()
                        continue
                    current_storage = storage[user_input - 1]
                    goods_stocks = DataAdapter.get_goods_stocks_by_storage(current_storage['id'])
                    print('Остатки номенклатуры на выбранном складе: ')
                    for idx, itm in enumerate(goods_stocks, 1):
                        current_goods = Goods.get_goods_by_id(itm['id_goods'], goods)
                        print(f'{idx}. {current_goods["name"]} {current_goods["color"]} '
                              f'{current_goods["manufacturer"]} по цене: {itm["price"]} остаток - {itm["count"]}')
                    print('Выберите номенклатуры для перемещения. Для выхода введите 0')
                    current_goods = []
                    while True:
                        user_input = input('Введите через пробел "проядковый номер номенклатуры" "количество": ')
                        if user_input.isdigit():
                            if int(user_input) == 0:
                                break
                        user_input = user_input.split(' ')
                        if len(user_input) != 2:
                            UserUIX.print_incorrect_input()
                            continue
                        if not user_input[0].isdigit() or not user_input[1].isdigit():
                            UserUIX.print_incorrect_input()
                            continue
                        current_goods_num = int(user_input[0])
                        if current_goods_num > len(goods_stocks):
                            UserUIX.print_incorrect_input()
                            continue
                        current_goods_id = goods_stocks[current_goods_num - 1]['id_goods']
                        current_goods_count = int(user_input[0])
                        if current_goods_count > goods_stocks[current_goods_num - 1]['count']:
                            print('Превышение остатка на складе!')
                            continue
                        current_goods.append(
                            {
                                'id_goods': current_goods_id,
                                'count': current_goods_count,
                            }
                        )
                    if len(current_goods) > 0:
                        while True:
                            user_input = input('Сохранить внутреннее перемещение в базу? 0 - нет 1 - да ')
                            if not user_input.isdigit():
                                UserUIX.print_incorrect_input()
                            if int(user_input) == 1:
                                inner_invoice = InnerInvoice(id_storage=current_storage['id'])
                                inner_invoice.goods = current_goods
                                DataAdapter.save_inner_invoice(inner_invoice.get_json())
                            break
                    break
                break

