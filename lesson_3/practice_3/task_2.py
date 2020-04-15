
def user_description(name: str, surname: str, year_of_birth: int, city: str, email: str, phone: str):
    """
    функция вывдоит информацию о пользователе
    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param year_of_birth: год рождения
    :param city: город рождения
    :param email: электронный адрес
    :param phone: телефон
    :return:
    """
    print(f'{name.title()} {surname.title()} {year_of_birth} года рождения, проживате в г.{city.title()}, '
          f'адрес эл. почты: {email}, контактный телефон: {phone}')


user_description(name='Иван', surname='Иванов', city='Волгоград', email='iivanov@mail.ru',
                 year_of_birth=1980, phone='+79662437753')