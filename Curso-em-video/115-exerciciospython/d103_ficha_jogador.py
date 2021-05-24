# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j="<desconhecido>", g=0):
    print(f"O jogador {j} fez {g} gols.")


j = input("Nome: ")
g = int(input("Nº de gols: "))
print(ficha(j, g))

