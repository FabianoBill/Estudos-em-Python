# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f"Digite o peso da {c}ª pessoa: "))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        else:
            menor = p
print(f"O maior peso foi {maior} kg e o menor foi {menor} kg.")

