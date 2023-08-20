def agrupar_em_intervalos(lista):
    if not lista:
        return []

    lista.sort()
    resultado = [[lista[0]]]

    for gol in range(1, len(lista)):
        if lista[gol] == lista[gol - 1] + 1:
            resultado[-1].append(lista[gol])
        else:
            resultado.append([lista[gol]])

    return resultado

entrada = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]
saida = agrupar_em_intervalos(entrada)
for intervalo in saida:
    if len(intervalo) == 1:
        print(f"[{intervalo[0]}]", end=", ")
    else:
        print(f"[{intervalo[0]}-{intervalo[-1]}]", end=", ")
