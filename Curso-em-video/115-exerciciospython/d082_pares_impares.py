# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []
while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua in "Nn":
        break

print(lista)
print(par)
print(impar)