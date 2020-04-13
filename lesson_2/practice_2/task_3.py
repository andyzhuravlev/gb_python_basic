
m_list = ['Зима', 'Весна', 'Лето', 'Осень']

m_dict = {0: 'Зима',
          1: 'Весна',
          2: 'Лето',
          3: 'Осень'
          }

month_int = 0
while True:
    while True:
        month = input('Введите номер месяца(для выхода введите exit): ')
        if month == 'exit':
            month_int = 0
            break
        if month.isdigit():
            month_int = int(month)
            if not (1 <= month_int <= 12):
                print('Некорректное значение месяца. Введите число от 1 до 12')
            else:
                break
        else:
            print('Введите число от 1 до 12')

    if month_int == 0:
        break

    month_int = 0 if month_int == 12 else month_int

    print(m_list[month_int // 3])
    print(m_dict.get(month_int // 3))
