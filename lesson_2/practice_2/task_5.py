
rate_list = [8, 7, 6, 3, 1]

new_item = 0
while True:
    value = input('Введите новое значение рейтинга(для выхода введите "exit"): ')
    if value == 'exit':
        new_item = -1
        break
    print(rate_list)
    if not value.isdigit():
        print('Введите число!')
        continue
    new_item = int(value)
    if new_item == 0: # если допустить значение 0, то rate_list.insert(len(rate_list), 0)
        print('Ведите значение больше 0!')
    else:
        break

if new_item > 0:
    for itm in rate_list[:]:
        if new_item > itm:
            rate_list.insert(rate_list.index(itm), new_item)
            break
    print(rate_list)