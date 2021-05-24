# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

números = []
def sorteia(n):
    from random import randint
    for c in range(0, 5):
        n.append(randint(0, 10))
    print(n)
def somaPar(n):
    par = 0
    for v in n:
        if v % 2 == 0:
            par += v
    print(par)

sorteia(números)
somaPar(números)
