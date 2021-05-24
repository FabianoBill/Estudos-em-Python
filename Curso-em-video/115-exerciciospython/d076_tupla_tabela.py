#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ("Lápis", 1.75, "Caneta", 2.00, "Caderno", 10.50, "Borracha", 0.50)
for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f"{tupla[c]:.<20} ", end="")
    else:
        print(f"R$ {tupla[c]:>5.2f}")
    