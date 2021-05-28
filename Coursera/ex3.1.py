# Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

n = int(input("Digite um número natural: "))
f = 1
for c in range(n, 0, -1):
    f *= c

print(f)
