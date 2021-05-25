def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s:  string a ser contada
    """
    caracteres_ordenados = sorted(s)
    caracter_anterior = caracteres_ordenados[0]
    cont = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            cont += 1
        else:
            print(f"{caracter_anterior}: {cont}")
            caracter_anterior = caracter
            cont = 1
    print(f"{caracter_anterior}: {cont}")


# digitando main o python já sugere --> if __name__ == '__main__':
if __name__ == '__main__':
    contar_caracteres('banana')