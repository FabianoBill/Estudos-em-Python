# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua in "Nn":
        break
print(f"Foram digitados {len(lista)} números.")
lista.sort(reverse=True)
print(f"A lista em ordem decrescente fica: {lista}.")
if 5 in lista:
    print("5 está na lista.")
else:
    print("5 não está na lista.")
