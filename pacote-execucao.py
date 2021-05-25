from pacote.biblioteca import modulo
print(modulo.funcao(4, 5))

from pacote.biblioteca.modulo import funcao
print(funcao(5, 6))

from pacote.biblioteca.modulo import funcao as soma
print(soma(6, 7))
