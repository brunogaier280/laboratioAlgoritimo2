
vendas = []
estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto : ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço unitário: "))
  
    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print(f"{nome} foi adicionado ao estoque.")

def buscar_produto():
    nome = input("Digite o nome do produto que deseja buscar: ")
    if nome in estoque:
        produto = estoque[nome]
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
        print(f"Preço unitário: R${produto['preco']:.2f}")
    else:
        print(f"{nome} não encontrado no estoque.")

def visualizar_produtos():
    print("Lista de produtos disponíveis:")
    for nome, info in estoque.items():
        print(f"Produto: {nome}")
        print(f"Quantidade em estoque: {info['quantidade']}")
        print(f"Preço unitário: R${info['preco']:.2f}")
        print()

def vender_produto():
    nome = input("Digite o nome do produto que foi vendido: ")
    if nome in estoque:
        quantidade_vendida = int(input("Digite a quantidade do produto vendida: "))
        produto = estoque[nome]
        if quantidade_vendida <= produto['quantidade']:
            valor_total = quantidade_vendida * produto['preco']
            produto['quantidade'] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de {nome} foram vendidas por R${valor_total:.2f}.")
            
            vendas.append({
                'produto': nome,
                'quantidade': quantidade_vendida,
                'valor_total': valor_total
            })
        else:
            print(f"Quantidade insuficiente de {nome} em estoque.")
    else:
        print(f"{nome}  produto não encontrado no estoque.")

def relatorio_vendas():
    print("Relatório de Vendas:")
    for venda in vendas:
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade vendida: {venda['quantidade']}")
        print(f"Valor total da venda: R${venda['valor_total']:.2f}")
        print()

while True:
    print("\nOpções:")
    print("1 - Adicionar um produto")
    print("2 - Buscar um produto")
    print("3 - Visualizar todos os produtos")
    print("4 - Vender um produto")
    print("5 - Relatório de Vendas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        buscar_produto()
    elif opcao == '3':
        visualizar_produtos()
    elif opcao == '4':
        vender_produto()
    elif opcao == '5':
        relatorio_vendas()
    elif opcao =='6':
        print("tchauu")
        break
    else:
        print("Opção inválida. use uma opção válida.")
