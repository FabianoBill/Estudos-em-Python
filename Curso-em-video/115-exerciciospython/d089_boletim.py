# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

bol = []
while True:
    nome = input("Nome: ")
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    media = (n1 + n2) / 2
    bol.append([nome, [n1, n2], media])
    continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua in "Nn":
        break
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for a, b in enumerate(bol):
    print(f'{a:<4}{b[0]:<10}{b[2]:>8}')
while True:
    indv = int(input("Digite o nº do aluno para seber suas notas. (999  interompe)"))
    if indv == 999:
        print("Finalizado")
        break
    if indv <= len(bol) - 1:
        print(f"As notas de {bol[indv][0]} são {bol[indv][1]}.")
