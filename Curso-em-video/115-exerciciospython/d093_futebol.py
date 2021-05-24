# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

cat = {}
cat['nome'] = input("Nome: ")
cat['partidas'] = int(input("Partidas jogadas: "))
pgols = []
tot = 0
for p in range(0, cat['partidas']):
    pgols.append(int(input(f"Gols na {p + 1}ª partida: ")))
cat['gols'] = pgols
cat['total'] = sum(pgols)
print(cat)
print("-=" * 30)
for k , v in cat.items():
    print(f"{k}: {v}")
print("-=" * 30)
print(f"O jogador {cat['nome']} jogou {cat['partidas']} partidas.")
for i, v in enumerate(cat['gols']):
    print(f"   Na {i + 1}ª partida, fez {v} gols.")
print(f"Somando um total de {cat['total']} gols.")