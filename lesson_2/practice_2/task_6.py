
# ОКЕИ — Общероссийский классификатор единиц измерения
# ресурс https://classifikators.ru/okei

unit_classifier = [{'id': 740, 'name': 'дюжина шт', 'description': 'Дюжина штук'},
                   {'id': 778, 'name': 'упак', 'description': 'Упаковка'},
                   {'id': 796, 'name': 'шт', 'description': 'Штука'}
                   ]

goods = []
while True:
    print('Введите информацию о товаре(для выхода введите "exit")')
    name = ''
    while True:
        name = input('Введите наименование товара: ')
        name = name.strip()
        if name != 'exit' or name != '':
            break
        else:
            print('Повторите ввод. Введена пустая строка!')
    if name == 'exit':
        break
    price = -1
    while True:
        price_value = input('Введите цену товара: ')
        if price_value == 'exit':
            price = -1
            break
        if price_value.isdigit():
            price = int(price_value)
            break
        print('Введите число!')
    if price == -1:
        break
    count = 0
    while True:
        count_value = input('Введите количество товара на складе: ')
        if count_value == 'exit':
            count = 0
            break
        if count_value.isdigit():
            count = int(count_value)
            if count == 0:
                print('Количество должно быть больше 0!')
                continue
            break
        print('Введите число!')
    if count == 0:
        break
    unit = -1
    for itm in enumerate(unit_classifier, 1):
        print(itm)
    while True:
        unit_id_value = input(f'Введите номер единицы измерения(от 1 до {len(unit_classifier)}): ')
        if unit_id_value == 'exit':
            unit = -1
            break
        if unit_id_value.isdigit():
            unit = int(unit_id_value)
            if unit == 0 or unit > len(unit_classifier):
                continue
            unit -= 1
            break
    if unit == -1:
        break

    goods.append((len(goods) + 1, {'наименование': name, 'цена': price, 'количество': count, 'ед': unit}))

if len(goods) > 0:
    goods_report = dict()
    for i in goods[0][1].keys():
        # goods_report.setdefault(i)
        # values = []
        # for itm in goods:
        #     if i == 'ед':
        #         values.append(unit_classifier[itm[1][i]]['name'])
        #     else:
        #         values.append(itm[1][i])
        # goods_report[i] = values
        var_keys = goods[0][1].keys()
        for itm in var_keys:
            goods_report.setdefault(itm)
            goods_report[itm] = []
        for itm in goods:
            for key in itm[1]:
                if key == 'ед':
                    goods_report[key].append(unit_classifier[itm[1][key]]['name'])
                else:
                    goods_report[key].append(itm[1][key])
    print(goods_report)

