# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

lista = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input("Sexo: [M/F] ").strip()[0]
    if pessoa['sexo'] not in "MmFf":
        pessoa['sexo'] = input("Favor digite apenas M ou F:")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua not in "SsNn":
        continua = input("Favor digite apenas S ou N: ")
    if continua in "Nn":
        break
media = soma / len(lista)
print(lista)
print(f"Foram cadastradas {len(lista)} pessoas.")
print(f"A média de idade é de {media}.")
print("As mulheres da lista são: ", end="")
for c in lista:
    if c['sexo'] in "Ff":
        print(f"{c['nome']}", end=" ")
print("\nAs pessoas com idade acima da média são: ", end="")
for c in lista:
    if c['idade'] > media:
        print(f"{c['nome']} idade {c['idade']} ", end="")        