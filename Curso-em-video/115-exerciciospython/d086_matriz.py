# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

# l1 = [[], [], []]
# l2 = [[], [], []]
# l3 = [[], [], []]
# for c in range(0, 9):
#     n = int(input(f"Digite o {c + 1}º número:"))
#     if 0 <= c <= 2:
#         l1[c].append(n)
#     if 3 <= c <= 5:
#         l2[c-3].append(n)
#     if 6 <= c <= 8:
#         l3[c-6].append(n)
# print(l1)
# print(l2)
# print(l3)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para [{l}, {c}]: "))

for l in range (0, 3):
    for c in range(0, 3):
            print(f"{matriz[l][c]:^5}", end="")
    print()
