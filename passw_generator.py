import random


def pasw_random(num):
    password = str()

    while len(password) < num:
        chars = random.choice('abcdefghijkmlnopqrstuvwxyz')
        numbers = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        password += chars
        password += str(numbers)

    print(password)


pasw_random(15)
