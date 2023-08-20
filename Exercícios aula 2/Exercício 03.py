
matriz = [
    [4, 9, 2],
    [8, 5, 1],
    [3, 6, 7]
]

soma_maiores = 0

for linha in matriz:
    
    maior_valor = max(linha)
    soma_maiores += maior_valor

print("A soma dos maiores valores de cada linha é:", soma_maiores)
