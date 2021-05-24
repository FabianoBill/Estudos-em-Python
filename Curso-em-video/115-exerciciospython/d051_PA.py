# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os primeiros termos dessa progressão.

a1 = int(input("1º termo da PA: "))
r = int(input("Rasão da PA: "))
n = int(input("Número de termos: "))
print("PA = ", end="")

for c in range(a1, a1 + n * r, r):
    print(c, end=" ")
