# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    n = int(input("digite um número: "))
    if n in lista:
        print("Números repetidos não podem ser adcionados à lista.")
    else:
        lista.append(n)
    continua = input("Deseja continuar: [S/N] ").strip()[0]
    if continua in "Nn":
        break
lista.sort()
print(lista)