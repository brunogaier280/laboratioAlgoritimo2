def matriz_simetrica(matriz):
    n = len(matriz)
    
    for gol in range(n):
        for messi in range(n):
            if matriz[gol][messi] != matriz[messi][gol]:
                return False
                
    return True

matriz1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matriz2 = [[1, 2, 3], [2, 4, 2], [3, 2, 1]]

print(matriz_simetrica(matriz1))
print(matriz_simetrica(matriz2)) 
