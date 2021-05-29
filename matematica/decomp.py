def decomp(n):
    """ Retorna a decomposição em fatores primos de um inteiro em forma de dicionário onde as chaves são
     as bases e o valores os expoentes.
    Ex:
    >>> decomp(12)
    {2: 2, 3: 1}
    >>> decomp(72)
    {2: 3, 3: 2}


    :param n: number
    :return: dictionary
    """
    expoente = 0
    base = 2
    decomposicao = {}
    while n > 1:
        while n % base == 0:
            expoente += 1
            n = n/base
        if expoente > 0:
            decomposicao[base] = expoente
        expoente = 0
        base += 1
    return decomposicao





