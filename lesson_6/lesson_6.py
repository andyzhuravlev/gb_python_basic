
# ООП

import random


class Homo:
    age = 0
    sex = random.choice(('m', 'f'))
    weight = 3400
    name = ''
    population = 0


vasya = Homo()
vasya.age = 21
vasya.name = 'Vasya'

