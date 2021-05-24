# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
menos20 = 0
maisvelho = 0
nomevelho = ""
media = 0
for c in range(1, 5):
    nome = input(f"Nome da {c}ª pessoa: ").strip()
    idade = int(input(f"idade da {c}ª pessoa: "))
    sexo = input(f"Sexo da {c}ª pessoa. M ou F: ").strip()
    soma += idade
    media = soma / c
    if sexo in "Mm" and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    elif sexo in "Ff":
        if idade < 20:
            menos20 += 1
print(media, nomevelho, menos20)
