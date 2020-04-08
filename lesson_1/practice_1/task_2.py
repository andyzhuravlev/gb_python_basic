
n_str = input("Enter time in seconds: ")
if n_str.isdigit():
    n_int = int(n_str)
    hour_int = int(n_int) // 3600
    n_int = n_int - hour_int * 3600
    minutes_int = n_int // 60;
    seconds_int = n_int - minutes_int * 60;
    time_str = f'{hour_int:>02}:{minutes_int:>02}:{seconds_int:>02}'
    print(time_str)
else:
    print('Incorrect value!')