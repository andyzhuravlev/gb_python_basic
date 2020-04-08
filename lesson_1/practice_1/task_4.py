
n_str = input('Enter number: ')
if n_str.isdigit():
    n_int = int(n_str)
    if n_int == 0 or n_int < 0:
        print('Enter number > 0')
    else:
        i = 0;
        max_int = 0;
        while n_int > 0:
            if n_int % 10 == 0:
                n_int = n_int // 10
                if max_int < i:
                    max_int = i
                i = 0
                # print(n_int)
            else:
                i += 1
                n_int -= 1
        print('Max int: ', max_int)
else:
    print('Incorrect value!')