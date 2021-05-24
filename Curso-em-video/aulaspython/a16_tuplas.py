lanche = ("Hambúrger", "Suco", "Pizza", "Pudim")

for comida in lanche:
    print(comida)

for contador in range(0, len(lanche)):
    print(lanche[contador], contador)

for posicao, comida in enumerate(lanche):
    print(comida, posicao)
