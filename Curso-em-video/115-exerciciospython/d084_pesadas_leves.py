# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves
dados = []
lista = []
max = min = 0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        max = min = dados[1]
    if dados[1] > max:
        max = dados [1]
    if dados[1] < min:
        min = dados[1]
    lista.append(dados[:])   
    dados.clear()
    continua = input("Deseja continuar: [S/N]").strip()[0]
    if continua in "Nn":
        break
print(f"Foram cadastradas {len(lista)} pessoas.")
print(f"O maior peso foi de {max}kg. Foi peso de: ", end="")
for p in lista:
    if p[1] == max:
        print(f"({p[0]}) ", end="")
print(f"\nO menor peso foi de {min}kg. Foi o peso de: ", end="")
for p in lista:
    if p[1] == min:
        print(f"({p[0]}) ", end="")

