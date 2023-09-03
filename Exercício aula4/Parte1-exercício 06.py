
def calcular_media(alunos, nome):
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        return media
    else:
        return "Aluno não encontrado"

alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou deixe em branco para sair): ")
    
    if nome == "":
        break
    
    notas = input(f"Digite as notas de {nome} separadas por espaço: ").split()
  
    notas = [float(nota) for nota in notas]
    
    alunos[nome] = notas
  
nome_aluno = input("Digite o nome do aluno para calcular a média: ")
media_aluno = calcular_media(alunos, nome_aluno)

if media_aluno != "Aluno não encontrado":
    print(f"A média de {nome_aluno} é: {media_aluno}")
else:
    print("Aluno não encontrado")
  
