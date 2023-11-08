
def verificar_tipo_triangulo(lado1,lado2,lado3):
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= 1: 
        raise ValueError ("o triangulo informado é invalido:")
    if lado1 == lado2 == lado3: 
        return "equilatero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
        return "isosceles"
    else: 
        return "escaleno" 

try: 
    lado1 = int(input("digite o primeiro lado do triangulo: "))
    lado2 = int(input("digite o segundo lado do triangulo: "))
    lado3 = int(input("digite o terceiro lado do triangulo: "))
    tipo = verificar_tipo_triangulo(lado1,lado2,lado3)
    print(f" o triangulo é {tipo}.")
except ValueError as e: 
    print(e)
            
        
        
