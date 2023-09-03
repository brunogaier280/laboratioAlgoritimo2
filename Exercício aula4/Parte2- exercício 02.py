
def contar_letras(frase):
  
    contagem_letras = {}

    frase = frase.lower().replace(" ", "")

    for letra in frase:
        
        if letra in contagem_letras:
            contagem_letras[letra] += 1
            contagem_letras[letra] = 1

    return contagem_letras

frase = 'Joao'
resultado = contar_letras(frase)
print(resultado)
