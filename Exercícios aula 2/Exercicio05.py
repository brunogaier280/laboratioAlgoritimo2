
def somar_matrizes(matriz1, matriz2):
    nova_matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for gol in range(3):
        for messi in range(3):
            nova_matriz[gol][messi] = matriz1[gol][messi] + matriz2[gol][messi]

    return nova_matriz

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = somar_matrizes(matriz1, matriz2)
print(resultado)
