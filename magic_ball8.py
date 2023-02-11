import random

number = random.randint(1, 9)
user = input('Ingrese su pregunta')
print(user)

if number == 1:
    print('Yes - definitely.')
elif number == 2:
    print('It is decidedly so.')
elif number == 3:
    print('Without a doubt')
elif number == 4:
    print('Reply hazy, try again')
elif number == 5:
    print('Better not tell you now')
elif number == 6:
    print('My sources say no')
elif number == 7:
    print('Outlook not so good')
elif number == 8:
    print('Very doubtfull')
else:
    print('Ask again')
