def vogal(str):
    """ Função que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
    >>> vogal('a')
    True
    >>> vogal('b')
    False
    >>> vogal('E')
    True

    :param str:
    :return:
    """
    vogais = ('a', 'e', 'i', 'o', 'u')
    if str.lower() in vogais:
        return True
    else:
        return False


