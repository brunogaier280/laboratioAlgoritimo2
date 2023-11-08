def find_element(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        raise IndexError("Índice inválido. O índice está fora dos limites da lista.")

minha_lista = [1, 2, 3, 4, 5]
indice = 7

try:
    resultado = find_element(minha_lista, indice)
    print("Elemento encontrado:", resultado)
except IndexError as e:
    print(e)
