def soma_elementos(lista):
    """ Recebe inteiros e devolve um inteiro correspondente a soma dos elementos da lista.
    >>> soma_elementos([1, 2, 4])
    7

    :param lista:
    :return:
    """
    soma = 0
    for i in lista:
        soma += i
    return soma
