# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
n = randint(0, 10)
a = int(input("Tente advinhar um número de 0 à 10: "))
c = 0
while a != n:
    a = int(input("Tente novamente: "))
    c += 1
print(f"Parabéns você acertou em {c} tentativas.")
