import random

words = ['python', 'desarrollo', 'javascript',
         'chipi', 'francisco', 'web', 'frutas', 'banana']
print(words)

select = random.choice(words)
answer = list()
life = 0

while True:
    user = input(
        'Ingrese una letra y si quiere adivinar la palabra escriba DONE')

    if user == 'DONE':

        word = input('Cual crees que es la palabra')

        if word == select:
            print(f'Ganaste la palabra era {select}')
            break
        if word != select:
            print('segui intentando')
            continue

    if user in select:
        answer.append(user)
        for i in answer:
            print(answer)
    else:
        print('Error')

    if user not in select:
        life += 1

    if life == 5:
        print('Perdiste usaste tus 5 vidas')
        break
