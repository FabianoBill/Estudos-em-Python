# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
# calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"

l = float(input("Digite o lado do quadrado: "))
p = 4*l
a = l**2
print(f"perímetro: {p} - área: {a}")
