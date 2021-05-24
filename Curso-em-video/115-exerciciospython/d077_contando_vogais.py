# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ("Abajur", "Bosque", "Caiaque", "Dado")
for palavra in lista:
    print(f"\nNa palavra {palavra} temos as vogais ", end="")
    for letra in palavra:
       if letra in "aeiou":
           print(f"{letra} ", end="")