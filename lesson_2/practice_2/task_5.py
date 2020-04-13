
rate_list = [8, 7, 6, 3, 1]

while True:
    print(rate_list)
    value = input('Введите новое значение рейтинга(для выхода введите "exit"): ')
    if value == 'exit':
        break
    if not value.isdigit():
        print('Введите число!')
        continue
    value = int(value)
