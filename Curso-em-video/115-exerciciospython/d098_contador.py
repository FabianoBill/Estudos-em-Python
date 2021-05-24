# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1  
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada

def contador(i, f, p):
    print("="* 30)
    if i < f and p > 0:
        while i <= f:
            print(i, end=" ")
            i += p
        print()
        print("="* 30)
    elif i > f and p < 0:
        while i > f:
            print(i, end=" ")
            i += p
        print()
        print("="* 30)
    else:
        print('Não é possivel com os valores selecionados.')


contador(1, 10, 1)
contador(10, 0, -2)
print("====Personalizado====")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)