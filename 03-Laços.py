
nome = "Fabiano"
print(nome[0], nome[2])

indice = 0
while indice < len(nome):
    print(nome[indice])
    indice += 1
print("="*30)
for valor in nome:
    print(valor)
for indice, valor in enumerate(nome):       #desenpacotamento
    print(indice, valor)


    