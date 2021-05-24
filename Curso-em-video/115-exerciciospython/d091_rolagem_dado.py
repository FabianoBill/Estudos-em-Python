# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
result = {"jogador1":randint(1, 6), "jogador2":randint(1, 6), 
"jogador3":randint(1, 6), "jogador4":randint(1,6)}
print(result)
ranking = []
ranking = sorted(result.items(), key=itemgetter(1), reverse=True)
print(ranking)
