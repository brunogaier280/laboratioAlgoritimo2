def soma_elementos_abaixo_diagonal(matriz):
    soma = 0
    for gol in range(len(matriz)):
        for messi in range(gol):
            soma += matriz[gol][messi]
    return soma


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = soma_elementos_abaixo_diagonal(matriz)
print("A soma dos elementos abaixo da diagonal principal é:", resultado)
