# Creo dict que contenga los puntajes de las casas
houses = dict.fromkeys(
    ['gryffindor', 'ravenclaw', 'hufflepuff', 'slytherin'], 0)

# Primera pregunta

q_1 = int(input(('''Do you like Dawn or Dusk?
      1) Dawn
      2) Dusk''')))

if q_1 == 1:
    houses['gryffindor'] += 1
    houses['ravenclaw'] += 1
elif q_1 == 2:
    houses['hufflepuff'] += 1
    houses['slytherin'] += 1
else:
    print('Incorrect input')

# Segunda pregunta

q_2 = int(input((''' When I m dead, I want people to remember me ass:
                 1) The good
                 2) The great
                 3) The wise
                 4) The bold''')))

if q_2 == 1:
    houses['hufflepuff'] += 1
elif q_2 == 2:
    houses['slytherin'] += 1
elif q_2 == 3:
    houses['ravenclaw'] += 1
elif q_2 == 4:
    houses['gryffindor'] += 1
else:
    print('Incorrect input')

# Tercera pregunta

q_3 = int(input(('''Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum''')))

if q_3 == 1:
    houses['slytherin'] += 1
elif q_3 == 2:
    houses['hufflepuff'] += 1
elif q_3 == 3:
    houses['ravenclaw'] += 1
elif q_3 == 4:
    houses['gryffindor'] += 1
else:
    ('incorrect input')

# Resultado
result = max(houses)
print(f'Tu casa va a ser... {result}')
