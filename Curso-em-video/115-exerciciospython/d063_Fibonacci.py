# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

# N = int(input("Escolha a quantidade de termos > 1 da sequência de Fibonacci que você quer exibir: "))
# an = 0
# aN = 1
# c = 2
# print("0 1", end="")
# while n < N:
#     an = an + aN
#     c += 1
#     print(f" {an}", end="")
#     aN = an + aN
#     if c == N:
#         break
#     c += 1
#     print(f" {aN}", end="")

N = int(input("Escolha a quantidade de termos > 1 da sequência de Fibonacci que você quer exibir: "))
an_2 = 0
an_1 = 1
c = 2
print("0 1", end="")
while c < N:
    an = an_1 + an_2
    an_2 = an_1
    an_1 = an
    print(f" {an}", end="")
    c += 1
