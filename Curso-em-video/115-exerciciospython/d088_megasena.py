# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
j = int(input("Quantos jogos você deseja sortear? "))
jogo = []
for j in range(0, j):
    c = 0
    while True:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            c += 1
        if c == 6:
            break
    jogo.sort()
    print(f"{(j + 1):2}º jogo {jogo}")
    jogo.clear()
