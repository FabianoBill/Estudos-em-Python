# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# saque = int(input("Qual o valor do saque: R$ "))
# c = saque // 50
# v = (saque % 50) // 20
# d = ((saque % 50) % 20) // 10
# u = (((saque % 50) % 20) % 10)
# print(f"Você ira receber {c} cédulas de cinquenta reais, {v} de vinte, {d} de dez e {u} de um.")

saque = int(input("Qual o valor do saque: R$ "))
tot = saque
c = 0
cedula = 50
while True:
    if tot >= cedula:
        tot -= cedula
        c += 1
    else:
        if c > 0:
            print(f"Total de {c} cédulas de {cedula} reais.")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        c = 0
        if tot == 0:
            break
