# Receba um número inteiro na entrada e imprima Fizz se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

n = int(input("Digite um número inteiro: "))
if n % 3 == 0:
    print("Fizz")
else:
    print(n)