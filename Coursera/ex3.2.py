# Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

n = int(input("Digite um número inteiro positivo: "))
c = 1
while c <= 2*n:
    print(c)
    c += 2

