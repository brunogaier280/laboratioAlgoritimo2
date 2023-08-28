
def calcular_notas_para_saque(valor_saque):
    notas_disponiveis = [100, 50, 20, 10]
    notas_entregues = []

    for nota in notas_disponiveis:
        while valor_saque >= nota:
            valor_saque -= nota
            notas_entregues.append(nota)
    
    return notas_entregues

def main():
    while True:
        valor_saque = int(input("Digite o valor do saque (ou 0 para sair): R$ "))
        if valor_saque == 0:
            break
        
        notas_entregues = calcular_notas_para_saque(valor_saque)
        print("Notas entregues:", notas_entregues)

if __name__ == "__main__":
    main()
  
