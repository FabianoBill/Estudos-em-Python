# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
min = max = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um número para a {c + 1}ª posição: ")))
    if c == 0:
        min = max = lista[c]
    else:
        if lista[c] > max:
            max = lista[c]
        if lista[c] < min:
            min = lista[c]
print(f"O maior número digitado foi {max} nas posição(ões): ", end="")
for pos, valor in enumerate(lista):
    if valor == max:
        print(f"{pos + 1} ", end="")
print(f"\nO menor número digitado foi {min} nas posilção(ões): ", end="")
for pos, valor in enumerate(lista):
    if valor == min:
        print(f"{pos + 1} ", end="")
