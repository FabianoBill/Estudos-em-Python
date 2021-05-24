# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior 
# [ 4 ] novos números [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
op = int(input('[1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa Escolha uma opção: '))
while op != 5:
    if op == 1:
        n = n1 + n2
        print(n)
    if op == 2:
        n = n1 * n2
        print(n)
    if op == 3:
        if n1 > n2:
            print(f"{n1} é maior")
        else:
            print(f"{n2} é maior")
    if op == 4:
        n1 = int(input("Digite o 1º número: "))
        n2 = int(input("Digite o 2º número: "))
    else:
        op = int(input('''Opção inválida
        [1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa Escolha uma opção: '''))
    op = int(input('[1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa Escolha uma opção: '))

print("Fim do progrma.")
