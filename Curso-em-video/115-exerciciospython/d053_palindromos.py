# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase: ").strip().upper().split()
junto = "".join(frase)
inv = ""
for l in range(len(junto) - 1, -1, -1):
    inv += junto[l]
if junto == inv:
    print(f"A frase formada pelas letras {junto} e seu inverso {inv} são palinromos.")
else:
    print(f"A frase formada pelas letras {junto} e seu inverso {inv} NÃO forma um palindromo.")
