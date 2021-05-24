# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

i = m = f = 0
while True:
    idade = int(input("Idade: "))
    if idade >= 18:
        i += 1
    sexo = " "
    while sexo not in "MmFf":
        sexo = input("Sexo: [M/F] ").strip()[0]
    if sexo in "Mm":
        m += 1
    elif sexo in "Ff" and idade < 20:
        f += 1
    continua = " "
    while continua not in "SsNn":
        continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua in "Nn":
        break
print(f"Foram cadastrados {i} pessoas com mais de 18, {m} homens e {f} mulheres com menos de 20 anos.")
