# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input("Quer saber a tabuada de qual número? "))
for c in range(1, 11):
    print(f"{n} x {c:2} = {n * c:2}")
    c += 1