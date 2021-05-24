# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

# n = int(input("Digite um número natural para saber seu fatorial: "))
# f = 1
# if n < 0:
#     print(f"{n} é negativo, não é um número natural, tente novamente.")
#     n = int(input("Digite um número natural para saber seu fatorial: "))
# print(f"{n}! = ", end="")
# while n > 0:
#     print(f"{n} ", end="")
#     print(" x " if n > 1 else " = ", end="")
#     f = f * n
#     n -= 1
# print(f)

n = int(input("Digite um número natural para saber seu fatorial: "))
f = 1
if n < 0:
    print(f"{n} é negativo, não é um número natural, tente novamente.")
    n = int(input("Digite um número natural para saber seu fatorial: "))
print(f"{n}! = ", end="")
for n in range(n, 0, -1):
    print(f"{n}", end="")
    print(" x " if n > 1 else "= ", end="")
    f = f * n
    n -= 1
print(f)
