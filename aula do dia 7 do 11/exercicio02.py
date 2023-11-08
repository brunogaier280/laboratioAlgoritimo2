def avaliar_produto(): 
    try: 
        nota = int(input("digite sua avaliaçaõ do produto de 0 a 10:"))
        assert 0 <= nota <= 10, "o numero deve estar de 0 a 10!"
        print(f" voce avaliou o produto com {nota} pontos.")
    except ValueError: 
        print("insira um numero inteiro! ")
    except AssertionError as e: 
        print(e)

avaliar_produto()
