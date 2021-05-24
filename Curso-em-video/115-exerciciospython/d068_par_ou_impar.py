# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
c = 0
while True:
    comp = randint(0, 5)
    n = int(input("Escolha um número de 0 à 5: "))
    pi = input("Escolha par ou impar: [P/I] ").strip()[0]
    if pi in "Pp":
        if (n + comp) % 2 != 0:
            break
    if pi in "Ii":
        if (n + comp) % 2 == 0:
            break
    print(f"Você escolheu {n} e o computador {comp}. Parabéns você ganhou.")
    c += 1
print(f"Você escolheu {n} e o computador {comp} e você perdeu, você teve {c} vitórias consecutivas.")