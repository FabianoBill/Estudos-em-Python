def maior_primo(n):
    """ Recebe n >= 2 e devolve o próximo número primo > n.
    Ex:
    >>> maior_primo(7)
    11
    >>> maior_primo(25)
    29

    :param n: number
    :return: number
    """
    while n >= 2:
        c = 0
        p = n + 1
        while 1 <= p <= n + 1:
            if (n + 1) % p == 0:
                c += 1
            p -= 1
        if c == 2:
            return n + 1
        n += 1


def menor_primo(n):
    """ Recebe n >= 2 e devolve o próximo número primo < n.
    Ex:
    >>> menor_primo(100)
    97
    >>> menor_primo(7)
    5

    :param n: number
    :return: number
    """
    while n >= 2:
        c = 0
        p = n - 1
        while 1 <= p <= n - 1:
            if (n - 1) % p == 0:
                c += 1
            p -= 1
        if c == 2:
            return n - 1
        n -= 1


