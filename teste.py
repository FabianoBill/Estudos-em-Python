def maior(probabilidades):

    # for indice in range(0, len(textos)):
    #     as_b = calcula_assinatura(textos[indice])
    #     probabilidades.append(compara_assinatura(ass_cp, as_b))
    for indice, valor in enumerate(probabilidades):
        if valor == max(probabilidades):
            return indice + 1
probabilidades = [1, 3, 5, 2, 4]
print(maior(probabilidades))