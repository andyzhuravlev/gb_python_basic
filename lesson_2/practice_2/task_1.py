
types = {type(1): 'Число',
         type('строка'): 'Строка',
         type(tuple()): 'Кортеж',
         type([]): 'Список',
         type(set()): 'Множество',
         type(dict()): 'Словарь',
         type(True): 'Булево',
         type(None): 'Неопределено',
         type(frozenset()): 'Неизменяемое множество',
         type(bytes()): 'Байты',
         type(bytearray()): 'Массив байт'
         }

lis = [1,
       'Строка',
       (2, 1, 2),
       [2, 1, 2],
       {3, 2, 2},
       {'key': 'value'},
       frozenset('блабла'),
       True,
       None,
       'string'.encode('utf-8'),
       bytearray(b'byte string')
       ]

for item in lis:
    t = type(item)
    type_description = types.get(t)
    type_description = 'Тип не определен !(' + str(t) if type_description is None else type_description
    print(f'{item}-{type_description}')
