#  Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

n = int(input("Digite um número inteiro positivo: "))
s = d = 0
while n > 0:
    d = n % 10
    s += d
    n //= 10
print(s)
