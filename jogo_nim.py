def computador_escolhe_jogada(n, m):
    comp_retira = 1
    while comp_retira <= m:
        r = n - comp_retira
        if r % (m + 1) == 0:
            print(f"O computador tirou {comp_retira} peça(s).")
            return comp_retira
        comp_retira += 1
    comp_retira = m
    print(f"O computador tirou {comp_retira} peça(s).")
    return comp_retira
def usuario_escolhe_jogada(n, m):
    usuario_retira = int(input("Quantas peças você vai tirar? "))
    while not 1 <= usuario_retira <= m:
        print("Oops! Jogada inválida! Tente de novo.")
        usuario_retira = int(input("Quantas peças você vai tirar? "))
    print(f"Você tirou {usuario_retira} peça(s).")
    return usuario_retira
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        while n != 0:
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                print(f"Fim do jogo! Você ganhou!")
                return "Você"
            else:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                print(f"\nFim do jogo! O computador ganhou!\n")
                return "O computador"
            else:
                print(f"Agora restam {n} peças no tabuleiro.\n")
    else:
        print("\nComputador começa!\n")
        while n > 0:
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                print(f"Fim do jogo! O computador ganhou!")
                return "O computador"
            else:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                print(f"Fim do jogo! Você ganhou!")
                return "Você"
            else:
                print(f"Agora restam {n} peças no tabuleiro.\n")
def campeonato():
    c =comp = v = 0
    print("\nVocê escolheu um campeonato!")
    for c in range(0, 3):
        print(f"\n**** Rodada {c+1} ****\n")
        a = partida()
        if a in "O computador":
            comp += 1
        else:
            v += 1
    print("\n**** Final do campeonato! ****\n")
    print(f"Placar: Você {v} X {comp} Computador")


print("\nBem-vindo ao jogo NIM! Escolha: \n")
partidas = int(input("Digite 1 para uma partida isolada ou 2 para um campeonato: "))
while not 1 <= partidas <= 2:
    partidas = int(input("Digite 1 ou 2: "))
if partidas == 1:
    partida()
elif partidas == 2:
    campeonato()
