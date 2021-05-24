from random import randint
from time import sleep
n = randint(0, 5) # O Computador sorteia um número inteiro de 0 à 5
num = int(input('Tente descobrir o número de 0 à 5 que o computador escolheu: ')) # O usuário escolhe um número
print('Processando...')
sleep(1.5)
if n == num:
    print('Parabens você acertou!!')
else:
    print('Você errou.')
print('Eu escolhi o número', n)