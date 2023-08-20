
matriz = [
    [4, 9, 2],
    [8, 5, 1],
    [3, 6, 7]
]

soma_total = 0
total_elementos = 0

for linha in matriz:

    soma_linha = 0
    elementos_linha = len(linha)

    for elemento in linha:
      
        soma_linha += elemento
        soma_total += elemento
        total_elementos += 1
  
    media_linha = soma_linha / elementos_linha
    print(f"A média da linha é: {media_linha}")

media_total = soma_total / total_elementos
print(f"A média total da matriz é: {media_total}")
