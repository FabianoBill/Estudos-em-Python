# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno["nome"] = input("Nome: ")
aluno["média"] = float(input("Média: "))
if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
elif aluno["média"] < 3:
    aluno["situação"] = "Reprovado"
else:
    aluno["situação"] = "Recuperação"    
print(aluno)