
def month(number): 
    ano = ("janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembreo","dezembro")
    print(f" o mes é {ano[number - 1]}meu querido usuario")
    
def value(retorno): 
    while True:
        try:
            value = int(input(retorno))
            if value > 12 or value == 0:
                print("digite um numero de 1 ate 12:")
                continue 
            return value
        except ValueError: 
            print("digite um numero valido:")
       
    
            


def main(): 
   number =  value("digite o numero que deseja saber o mes:")
   month(number)
    
    
    
main()
