# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.       

def escreva(msg):
    l = len(msg) + 4
    print('-'* l)
    print(f'  {msg}  ')
    print('-'* l)


escreva("Olá mundo!")
