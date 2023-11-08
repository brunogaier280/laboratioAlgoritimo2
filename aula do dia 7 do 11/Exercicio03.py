def calcular_raiz(numero):
    if numero < 0:
        raise Exception("A raiz quadrada de números negativos não é real.")
    else:
        return numero** (1/2)


try:
    num = float(input("Digite um número: "))
    resultado = calcular_raiz(num)
    print(f"A raiz quadrada de {num} é {resultado}")
except Exception as e:
    print(e)
except ValueError:
    print("Por favor, digite um número válido.")
