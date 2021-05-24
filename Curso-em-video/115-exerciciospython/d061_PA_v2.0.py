# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

# a1 = int(input("Qual o 1º termo da PA? "))
# r = int(input("Qual a rasão da PA? "))
# n = 1
# print("PA = {", end="")
# while n <= 10:
#     an = a1 + (n - 1) * r
#     if n == 10:
#         print("", an, "}", end="")
#     else:
#         print(f" {an},", end="")
#     n += 1

a1 = int(input("Qual o 1º termo da PA? "))
r = int(input("Qual a rasão da PA? "))
an = a1
c = 1
while c <= 10:
    print(f" {an}", end="")
    an += r
    c += 1
print("\nPAUSA")
