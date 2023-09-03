filmes = {
    'Matrix': {'vilão': 'Agente Smith', 'ano de lançamento': 1999},
    'Star Wars: Episódio IV': {'vilão': 'Darth Vader', 'ano de lançamento': 1978},
    'O Senhor dos Anéis: A Sociedade do Anel': {'vilão': 'Sauron', 'ano de lançamento': 2001},
    '007: Skyfall': {'vilão': 'Raoul Silva', 'ano de lançamento': 2012},
    'Pantera Negra': {'vilão': 'Erik Killmonger', 'ano de lançamento': 2018}
}

for filme, info in filmes.items():
    print(f"Filme: {filme}")
    print(f"Vilão: {info['vilão']}")
    print(f"Ano de lançamento: {info['ano de lançamento']}")
    print()
