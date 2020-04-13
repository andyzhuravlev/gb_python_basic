
input_str = input('Введите строку, состоящую из нескольких строк: ')
lis = input_str.split(' ')

for ind, item in enumerate(lis, 1):
    print(ind, item[:10])
