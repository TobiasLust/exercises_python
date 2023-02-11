
shopping_list = []

while True:
    item = input(
        
        "Ingrese el elemento a agregar a la lista de compras (escriba 'done' para terminar): ")
    if item == 'done':
        break
    else:
        shopping_list.append(item)


print("Lista de compras:", shopping_list)

