import datetime

estoque = {} 
historico = []

def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço unitário: "))
    categoria = input("Categoria do produto: ")

    if nome in estoque:
        estoque[nome]["quantidade"] += quantidade
    else:
        estoque[nome] = {"quantidade": quantidade, "preco": preco, "categoria": categoria}

    print("Produto adicionado com sucesso!")

def alterar_valor_produto():
    nome = input("Nome do produto: ")
    novo_preco = float(input("Novo preço unitário: "))

    if nome in estoque:
        estoque[nome]["preco"] = novo_preco
        print("Preço do produto atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

def informacao_vendas_produto():
    nome = input("Nome do produto para exibir informações de vendas: ")

    if nome in estoque:
        produto = estoque[nome]
        print(f"Produto: {nome}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']}, Categoria: {produto['categoria']}")
        
        vendas_produto = filter(lambda venda: nome in venda['produto'], historico)
        
        if vendas_produto:
            print("\nHistórico de vendas para este produto:")
            for venda in vendas_produto:
                print(f"Quantidade: {venda['quantidade']}, Valor Total: R$ {venda['valor_total']}, Data da Venda: {venda['data_venda']}")
        else:
            print("Nenhuma venda registrada para este produto.")
    else:
        print("Produto não encontrado.")

def excluir_produto():
    nome = input("Nome do produto a ser excluído: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

def visualizar_produtos_por_categoria():
    categoria_desejada = input("Digite a categoria desejada: ")
    
    for produto, info in estoque.items():
        if info['categoria'] == categoria_desejada:
            print(f"Produto: {produto}, Quantidade: {info['quantidade']}, Preço: R$ {info['preco']}, Categoria: {info['categoria']}")

def vender_produto():
    nome = input("Nome do produto vendido: ")
    quantidade_vendida = int(input("Quantidade vendida: "))

    if nome in estoque and estoque[nome]["quantidade"] >= quantidade_vendida:
        estoque[nome]["quantidade"] -= quantidade_vendida 
        valor_total = quantidade_vendida * estoque[nome]["preco"]
        data_venda = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historico.append({"produto": nome, "quantidade": quantidade_vendida, "valor_total": valor_total, "data_venda": data_venda})

        print(f"Venda realizada com sucesso! Total: R$ {valor_total}")
    else:
        print("Produto não encontrado ou quantidade insuficiente em estoque.")

while True:
    print("\n===== Sistema de Gerenciamento de Estoque =====")
    print("1. Adicionar Produto")
    print("2. Alterar Valor de Produto")
    print("3. Excluir Produto")
    print("4. Vender Produto")
    print("5. Visualizar Todos os Produtos")
    print("6. Relatório de Vendas")
    print("0. Sair")
    print("7. Visualizar Produtos por Categoria")
    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        alterar_valor_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        vender_produto()
    elif opcao == "5":
        for produto, info in estoque.items():
            print(f"Produto: {produto}, Quantidade: {info['quantidade']}, Preço: R$ {info['preco']}, Categoria: {info['categoria']}")
    elif opcao == "6":
        for venda in historico:
            print(f"Produto: {venda['produto']}, Quantidade: {venda['quantidade']}, Valor Total: R$ {venda['valor_total']}, Data da Venda: {venda['data_venda']}")
    elif opcao == "7":
        visualizar_produtos_por_categoria()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
