# Datos del usuario
codes = {200, 232, 211, 100, 202}
balance = 10000


# Se le pide codigo de seguridad de su tarjeta

print('Ingrese su codigo de seguridad...')
code_enter = int(input())

for pin in codes:
    if pin == code_enter:
        print('Login....')
        print('''Buenos dias, que accion quiere realizar...
        1. Transferencia
        2. Ver Saldo
        3. Retirar''')
        action = int(input())
        if action == 1:
            print('¿Cuanto desea transferir?..')
        if action == 2:
            print(f'Su saldo es {balance}')
        if action == 3:
            print('¿Cuanto desea retirar?')
            withdraw = int(input())
            print(f'''Usted retira: {withdraw}
          Su saldo actual es de : {balance - withdraw}''')
        break
else:
    print('Intente de nuevo...')
