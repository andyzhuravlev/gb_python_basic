
n_str = input('Enter number: ')
if n_str.isdigit():
    result_int = int(n_str) + int(n_str * 2) + int(n_str * 3)
    print(result_int)
else:
    print('Incorrect value!')