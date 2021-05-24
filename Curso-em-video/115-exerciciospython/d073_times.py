# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times.b) Os últimos 4 colocados.c) Times em ordem alfabética.d) Em que posição está o time da Chapecoense.
times = ("a", "e", "i", "o", "u", "b", "c", "d", "f", "g")
print("Os 5 primeiros colocados são: ", times[:5])
print("Os 4 últimos colocados são: ", times[-4:])
print("Times em ordem alfabética: ", sorted(times))
print(f"O time c está na {times.index('c') + 1}ª posição.")