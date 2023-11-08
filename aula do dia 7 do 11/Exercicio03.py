def calculate_square_root(number):
    if number < 0:
        raise Exception("A raiz quadrada de números negativos não é real.")
    else:
        return number ** (1/2)

# Exemplo de uso da função:
try:
    num = float(input("Digite um número: "))
    resultado = calculate_square_root(num)
    print(f"A raiz quadrada de {num} é {resultado}")
except Exception as e:
    print(e)
except ValueError:
    print("Por favor, digite um número válido.")
