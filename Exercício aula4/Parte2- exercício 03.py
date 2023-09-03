
alunos_notas = {}

while True:
    nome = input("Digite o nome do aluno (ou 'oooo' para encerrar): ")
    
    if nome == 'oooo':
        break
    
    nota = float(input("Digite a nota do aluno: "))
    
    alunos_notas[nome] = nota

if alunos_notas:
    aluno_maior_nota = max(alunos_notas, key=alunos_notas.get)
    maior_nota = alunos_notas[aluno_maior_nota]
    print(f"O aluno com a maior nota é {aluno_maior_nota} com nota {maior_nota}")
else:
    print("Nenhum aluno foi registrado.")
  
