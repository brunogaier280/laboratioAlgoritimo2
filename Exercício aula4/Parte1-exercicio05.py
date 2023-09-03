def contar_vogais(texto):
    
    contagem_vogais = {}

    vogais = "AEIOUaeiou"
  
    for caractere in texto:
        
        if caractere in vogais:
            
            if caractere in contagem_vogais:
                contagem_vogais[caractere] += 1
          
            else:
                contagem_vogais[caractere] = 1

    return contagem_vogais

texto = "Isso é um exemplo de contagem de vogais"
resultado = contar_vogais(texto)
print(resultado)
