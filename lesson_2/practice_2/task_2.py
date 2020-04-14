
lis = []
while True:
    value = input('Введите значение элемента (для завершения введите "exit"): ')
    if value == 'exit':
        break
    value = value if not value.isdigit() else int(value)
    lis.append(value)

print(lis)

i = 0
count = len(lis)
while i < count:
    if i == count - 1 and count / 2 != 0:
        break
    # tmp = lis[i]
    # lis[i] = lis[i + 1]
    # lis[i + 1] = tmp
    lis[i], lis[i + 1] = lis[i + 1], lis[i]
    i += 2

print(lis)