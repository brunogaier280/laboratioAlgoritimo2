
def inverter_lista(lista):
    nova_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista

lista_original = [1, 2, 3, 4, 5]
lista_invertida = inverter_lista(lista_original)
print(lista_invertida) 
