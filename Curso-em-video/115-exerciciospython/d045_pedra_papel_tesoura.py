from random import choice
p = input("\n Tente ganhar do computador.\n Escolha: pedra, papel ou tesoura: ").strip().lower()
c = choice(['pedra', 'papel', 'tesoura'])
if p != 'pedra' and p != 'papel' and p != 'tesoura':
    print("Escolha inválida.")
elif c == p:
    print(f" O computador escolheu {c} e você {p}. Deu EMPATE.")
elif c == 'pedra' and p == 'tesoura':
    print(f" O computador escolheu {c} e você {p}. Você PERDEU.")
elif c == 'papel' and p == 'pedra':
    print(f" O computador escolheu {c} e você {p}. Você PERDEU.")
elif c == 'tesoura' and p == 'papel':
    print(f" O computador escolheu {c} e você {p}. Você PERDEU.")
else:
    print(f" O computador escolheu {c} e você {p}. Você GANHOU.")
