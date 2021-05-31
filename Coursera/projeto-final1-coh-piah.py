import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
    textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)



def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# def compara_assinatura(as_a, as_b):
#     '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
#     nas assinaturas.'''
#
#
#     le_assinatura()
#     wal
#     ttr
#     hlr
#     sal
#     sac
#     pal
#
#
#
def calcula_assinatura(texto):
    ''' Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto)
    print('sent\n', sentencas)
    frases = []
    for indice in range(0, len(sentencas)):
        frases.append(separa_frases(sentencas[indice]))
    print('frases\n', frases)
    palavras = []
    for indice in range(0, len(frases)):
        for indice2 in range(0, len(frases[indice])):
            palavras.append(separa_palavras(frases[indice][indice2]))
    print('palavras\n', palavras)
    caracteres = []
    for indice in range(0, len(palavras)):
        for indice2 in range(0, len(palavras[indice])):
            palavras[indice][indice2].split()
            for indice3 in range(0, len(palavras[indice][indice2])):
                palavras[indice][indice2][indice3].split()
                caracteres.append(palavras[indice][indice2][indice3])
    caracteresf = []
    for indice in range(0, len(frases)):
        for indice2 in range(0, len(frases[indice])):
            frases[indice][indice2].split()
            for indice3 in range(0, len(frases[indice][indice2])):
                frases[indice][indice2][indice3].split()
                caracteresf.append(frases[indice][indice2][indice3])

    caracteress = []
    for indice in range(0, len(sentencas)):
        for indice2 in range(0, len(sentencas[indice])):
            sentencas[indice][indice2].split()
            for indice3 in range(0, len(sentencas[indice][indice2])):
                sentencas[indice][indice2][indice3].split()
                caracteress.append(sentencas[indice][indice2][indice3])




    palavras_separadas = []
    for indice in range(0, len(palavras)):
        for indice2 in range(0, len(palavras[indice])):
            palavras_separadas.append(palavras[indice][indice2])


    npu = n_palavras_unicas(palavras_separadas)
    npd = n_palavras_diferentes(palavras_separadas)

    print('npu ', npu)
    print('npd ', npd)







    tot_sentencas = len(sentencas)
    print('tot sent', tot_sentencas)
    tot_palavras = 0
    for indice in range(0, len(palavras)):
        tot_palavras += len(palavras[indice])
    print(tot_palavras)
    tot_frases = 0
    for indice in range(0, len(frases)):
        tot_frases += len(frases[indice])
    print('tot frases', tot_frases)
    # tot_palavras = 0
    # for indice in range(0, len(palavras)):
    #     tot_palavras += len(palavras[indice])
    # print('tot palavras', tot_palavras)
    # tot_caracteres = 0
    # for indice in range(0, len(palavras)):
    #     for indice2 in range(0, len(palavras[indice])):
    #         tot_caracteres += len(palavras[indice][indice2])
    tot_caracteres = len(caracteres)
    print('tot carac', tot_caracteres)
    tot_caracteresf = len(caracteresf)
    print('tot carac', tot_caracteresf)
    tot_caracteress = len(caracteress)
    print('tot carac', tot_caracteress)
    wal1 = tot_caracteres/tot_palavras
    ttr1 = npd/tot_palavras
    hlr1 = npu/tot_palavras
    sal1 = tot_caracteress/tot_sentencas
    sac1 = tot_frases/tot_sentencas
    pal1 = tot_caracteresf/tot_frases
    return [wal1, ttr1, hlr1, sal1, sac1, pal1]


# def avalia_textos(textos, ass_cp):
#     '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n)
#     do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
texto2 = "O gato caçava o rato"
print(calcula_assinatura(texto))
