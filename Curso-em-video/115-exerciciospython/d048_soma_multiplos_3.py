# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

acumulador = 0
contador = 0
for c in range(1, 500, 2):      # impares
    if c % 3 == 0:               # múltiplos de 3
        acumulador += c
        contador += 1
print(f"\nA soma de todos os {contador} números solicitados é {acumulador}")
