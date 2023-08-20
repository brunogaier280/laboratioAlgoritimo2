
def separar_duplicados_e_unicos(lista):
    duplicados = []
    unicos = []

    for elemento in lista:
        if lista.count(elemento) > 1:
            if elemento not in duplicados:
                duplicados.append(elemento)
        else:
            unicos.append(elemento)

    return duplicados, unicos

lista_original = [1, 2, 2, 3, 4, 4, 5, 6]
duplicados, unicos = separar_duplicados_e_unicos(lista_original)
print("Duplicados:", duplicados)
print("Únicos:", unicos)
