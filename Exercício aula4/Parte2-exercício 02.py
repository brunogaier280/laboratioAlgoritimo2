
semana = {
    'Segunda-feira': ['Aula de Matemática', 'Aula de História'],
    'Terça-feira': ['Aula de Ciências', 'Aula de Inglês'],
    'Quarta-feira': ['Aula de Português', 'Aula de Educação Física'],
    'Quinta-feira': ['Aula de Geografia', 'Aula de Artes'],
    'Sexta-feira': ['Aula de Química', 'Aula de Informática'],
    'Sábado': [],
    'Domingo': []
}


print("Minha agenda da semana é a seguinte:")
for dia, aulas in semana.items():
    if aulas:
        print(f"{dia}: {', '.join(aulas)}")
    else:
        print(f"{dia}: Sem aulas")
