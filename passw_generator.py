import random


def pasw_random(num):
    chars = 'abcdefghijkmlnopqrstuvwxyz'
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    password = str()

    while len(password) < num:
        letra = random.choice(chars)
        numero = random.choice(numbers)
        password += letra
        password += str(numero)

    print(password)


pasw_random(15)
