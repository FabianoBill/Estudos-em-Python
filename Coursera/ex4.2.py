# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

def maior_primo(n):
    """ Recebe um inteiro >= 2 como parâmetro e devolve o maior número primo <= ao número passado.
    Ex:
    >>> maior_primo(100)
    97
    >>> maior_primo(7)
    7

    :param n: number
    :return: number
    """
    while n >= 2:
        c = 0
        p = n
        while 0 < p <= n:
            if n % p == 0:
                c += 1
            p -= 1
        if c == 2:
            return n
        n -= 1
