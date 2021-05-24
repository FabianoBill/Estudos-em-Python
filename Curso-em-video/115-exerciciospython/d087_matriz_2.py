# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Spares = S3c = max2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f"Digite o termo [{l}, {c}]: "))
        if mat[l][c] % 2 == 0:
            Spares += mat[l][c]
        if c == 2:
            S3c += mat[l][c]
        if l == 1 and c == 0:
            max2 = mat[l][c]
        if l == 1 and mat[l][c] > max2:
            max2 = mat[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{mat[l][c]:^6}", end="")
    print()
print(f"A soma dos elementos pares dessa matriz é {Spares}.")
print(f"A soma dos elementos da 3ª coluna é {S3c}.")
print(f"O maior elemento da 2ª linha é {max2}.")