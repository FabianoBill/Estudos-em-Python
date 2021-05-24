# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

c = soma = n = 0
while True:
    n = int(input("Gigite um número inteiro: [999 para parar] "))
    if n == 999:
        break
    soma += n
    c += 1

print(f"A soma dos {c} números digitados é {soma}.")