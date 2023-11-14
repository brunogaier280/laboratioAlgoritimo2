
file = open('numeros.txt', 'r')
numeros = file.read().split(',')
file.close()


numeros = [float(numero) for numero in numeros]
soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(f'A média dos números é: {media}')
