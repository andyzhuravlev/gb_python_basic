
rate_list = [8, 7, 6, 3, 1]

new_item = 0
while True:
    print(rate_list)
    value = input('Введите новое значение рейтинга(для выхода введите "exit"): ')
    if value == 'exit':
        break
    if not value.isdigit():
        print('Введите число!')
        continue
    new_item = int(value)
    if new_item == 0:
        print('Ведите значение больше 0!')
    else:
        break

for itm in rate_list[:]:
    if new_item > itm:
        rate_list.insert(rate_list.index(itm), new_item)
        break

print(rate_list)