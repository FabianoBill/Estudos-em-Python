# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

l = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
while True:
     n = int(input("Digite um número de 0 à 10: "))
     if 0 <= n <= 10:
          continua = input(f"Voce digitou o número {l[n]}. Deseja continuar? [S/N] ").strip()[0]
     if continua in "Nn":
          break
     if n < 0 or n > 10:
          print("Tente novamente. ", end="")

print("Fim.")
