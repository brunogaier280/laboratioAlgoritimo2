ef division(val1,val2): 
    try: 
        return val1 / val2 
    except ZeroDivisionEroror:
        print('[erro] voce nao pode dividir um numero por zero!')
    except BaseException as error : 
        print(f'[erro] ocorreu um erro:{erro}')
        
def input_int(): 
    value = int(input("digite um valor:"))
    return value 
    
def main(): 
    try:
        number_one = int (input("digite um numero:"))
        number_two = int(input("digite outro numero:"))
        
        result = division(number_one,number_two)
    
        print(f'resultado:{result}')
    except ValueError: 
        print('[erro] numero informado invalido!')
    except BaseException as erro: 
         print(f'[erro] ocorreu um erro:{erro}')


main()

