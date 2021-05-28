def contar_caracteres(s):
    """Função que conta os caracteres de uma string
    Ex:
    >>> contar_caracteres('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:  string a ser contada
    """

    resultado = {}
    for caracter in s:
        # contagem = resultado.get(caracter, 0)
        # contagem += 1
        # resultado[caracter] = contagem
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado


# digitando main o python já sugere --> if __name__ == '__main__':
if __name__ == '__main__':
    print(contar_caracteres('banana'))



# def contar_caracteres(s):
#     """Função que conta os caracteres de uma string
#     Ex:
#     >>> contar_caracteres('banana')
#     {'a': 3, 'b': 1, 'n': 2}
#
#     :param s:  string a ser contada
#     """
#     caracteres_ordenados = sorted(s)
#     caracter_anterior = caracteres_ordenados[0]
#     cont = 1
#     resultado = {}
#     for caracter in caracteres_ordenados[1:]:
#         if caracter == caracter_anterior:
#             cont += 1
#         else:
#             resultado[caracter_anterior] = cont
#             caracter_anterior = caracter
#             cont = 1
#     resultado[caracter_anterior] = cont
#     return resultado
#
#
# # digitando main o python já sugere --> if __name__ == '__main__':
# if __name__ == '__main__':
#     print(contar_caracteres('banana'))