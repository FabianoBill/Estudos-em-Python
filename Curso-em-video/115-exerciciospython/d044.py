preco = float(input("Qual o valor a ser pago? "))
pg = int(input('''[ 1 ] dinheiro ou cheque
[ 2 ] á vista no cartão
[ 3 ] no cartão em 2X
[ 4 ] no cartão em 3X ou mais
Das opções acima, escolha a forma de pagamento: '''))
if pg == 1:
    print("Valor final: R$ {:.2f}".format(preco*0.9))
elif pg == 2:
    print("Valor final: R$ {:.2f}".format(preco*0.95))
elif pg == 3:
    print("Valor final: R$ {:.2f}".format(preco))
elif pg == 4:
    print("Valor final: R$ {:.2f}".format(preco*1.2))
else:
    print("Opção inválida.")
