
name_str = input('Enter your name: ')
print('Hello ', name_str)

age_str = input('How old are you? ')
if age_str.isdigit():
    result_str = f'Hello {name_str}, {age_str} years old.'
    print(result_str)
else:
    print('incorrect input!')