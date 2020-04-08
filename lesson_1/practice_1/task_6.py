
progress_int = 10
a_str = input('Enter first day result: ')
if a_str.isdigit():
    b_str = input('Enter minimal result: ')
    if b_str.isdigit():
        a_fl = float(a_str)
        b_fl = float(b_str)
        if b_fl == a_fl:
            print('minimal result = first day result')
        elif b_fl < a_fl:
            print('first day result > minimal result')
        else:
            print(f'1 day: {a_fl:.2f}')
            i = 1;
            while a_fl < b_fl:
                i += 1
                a_fl = a_fl + a_fl * progress_int / 100;
                print(f'{i} day: {a_fl:.2f}')
    else:
        print('Incorrect minimal result!')
else:
    print('Incorrect day result value!')