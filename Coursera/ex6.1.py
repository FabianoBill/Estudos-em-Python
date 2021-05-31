def remove_repetidos(lista):
    """ Recebe uma lista de inteiros e remove os repetidos e retorna uma lista ordenada.
        >>> remove_repetidos([2, 4, 2, 2, 3, 3, 1])
        [1, 2, 3, 4]
        >>> remove_repetidos([1, 2, 3, 3, 3, 4])
        [1, 2, 3, 4]


    :param lista: list
    :return: list
    """
    lista.sort()
    i = 0
    while i < len(lista) - 1:
        if lista[i] == lista[i + 1]:
            del lista[i + 1]
            i -= 1
        i += 1
    return lista
