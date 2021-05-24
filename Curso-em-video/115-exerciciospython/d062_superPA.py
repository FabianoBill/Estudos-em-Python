# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

a1 = int(input("Qual o 1º termo da PA? "))
r = int(input("Qual a rasão da PA? "))
an = a1
n = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while n <= tot:
        print(f" {an}", end="")
        an += r
        n += 1
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))
