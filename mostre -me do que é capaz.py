
vetor = []

opcao = 0

while opcao != 4:
    
    print("-------- MENU --------")
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Sair")
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:
        item = input("Digite o item que deseja inserir: ")
        vetor.append(item)
        print("Item inserido com sucesso!")
        
    elif opcao == 2:
        if len(vetor) == 0:
            print("Não há itens para retirar!")
        else:
            item = input("Digite o item que deseja retirar: ")
            if item in vetor:
                vetor.remove(item)
                print("Item retirado com sucesso!")
            else:
                print("Item não encontrado no vetor.")
                
    elif opcao == 3:
        if len(vetor) == 0:
            print("Não há itens para listar!")
        else:
            print("Itens do vetor:")
            for item in vetor:
                print(item)
    elif opcao == 4:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Digite novamente.")
