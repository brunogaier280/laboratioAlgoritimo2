
pessoas_proximas = {
    'rogério': 'Azul',
    'amaral': 'Verde',
    'oswaldo': 'Vermelho',
    'geraldo': 'Amarelo',
    'nilmar': 'Roxo'
}

print("As 5 pessoas mais próximas de mim e as cores de suas camisas são:")
for nome, cor_camisa in pessoas_proximas.items():
    print(f"{nome}: {cor_camisa}")
