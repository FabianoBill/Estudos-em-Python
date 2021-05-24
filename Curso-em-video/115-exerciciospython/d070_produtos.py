# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

c = menor = mil = soma = 0
barato = " "
while True:
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço: R$ "))
    soma += preco
    c += 1
    if preco > 1000:
        mil += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = nome
    if preco > 1000:
        mil += 1
    continua = " "
    while continua not in "SsNn":
        continua = input("Continua? [S/N] ").strip()[0]
    if continua in "Nn":
        break
print(f"O total gasto foi R$ {soma:.2f}. {mil} produtos custam mais de R$ 1000,00 e {barato} é o produto mais barato. ")
