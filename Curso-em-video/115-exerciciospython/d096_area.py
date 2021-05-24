# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(b, h):
    a = b * h
    print(f"A área do terreno é igua a {a:.1f} m².")


b = float(input("Largura (m): "))
h = float(input("Altura (m): "))

área(b, h)
