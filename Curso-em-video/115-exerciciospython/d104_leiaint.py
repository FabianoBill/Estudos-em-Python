# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    while True:
        str = input(msg)
        if str.isnumeric():
            valor = int(str)
            break
        else:
            print("ERRO! Só são aceitos números inteiros.")
    return valor

i = leiaint("Digite um nº inteiro: ")
print(i)
