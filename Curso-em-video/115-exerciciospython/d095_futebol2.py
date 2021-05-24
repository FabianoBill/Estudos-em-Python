# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jog = {}
time = []
while True:
    jog['nome'] = input("Nome: ")
    jog['partidas'] = int(input("Partidas jogadas: "))
    gpart = []
    for p in range(0, jog['partidas']):
        gpart.append(int(input(f"Gols na {p + 1}ª partida: ")))
    jog['gols'] = gpart
    jog['total'] = sum(gpart)
    time.append(jog.copy())
    continua = input("Deseja continuar? [S/N] ").strip()[0]
    if continua in "Nn":
        break
    if continua not in "Ss":
        input("Digite apenas S ou N").strip()[0]
print(time)
print("-=" * 30)
for k in jog.keys():
    print(f'{k:^10}', end="")
print()
print("-=" * 30)
for c , d in enumerate(time):
    print(f"{c}", end="")
    for v in d.values():
        print(f"{str(v):^10}", end="")
    print()
print("-=" * 30)
while True:
    j = int(input("Mostrar detalhes de qual jogador? (999 parar) "))
    if j == 999:
        break
    print(f"Gols feitos em cada partida por {time[j]['nome']}.")
    for i, g in enumerate(time[j]['gols']):
        print(f"No {i + 1}º jogo fez {g} gols.")
print("Obrigado. Fim.")
