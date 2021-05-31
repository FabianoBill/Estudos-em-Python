#
# palavras = [['a', 'bc'], ['d'], ['e', 'fg', 'hi']]
# tot_palavras = 0
# for indice in range(0, len(palavras)):
#     tot_palavras += len(palavras[indice])
# print(tot_palavras)
def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()
texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

print(separa_palavras(texto))



# palavras_separadas = texto.split()
# print('palavras\n', palavras_separadas)
# tot_palavras = len(palavras_separadas)
# caracteres_separados = []
# for indice in range(0, len(palavras_separadas)):
#     palavras_separadas[indice].split()
#     for indice2 in range(0, len(palavras_separadas[indice])):
#         caracteres_separados.append(palavras_separadas[indice][indice2])
# # tot_caracteres = len(caracteres_separados)
# print(caracteres_separados)