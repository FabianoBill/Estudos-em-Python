# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

n = input("Digite uma expressão que use apensa paresnteses: ")
a = b = 0
for pos, valor in enumerate(n):
    if valor in "(":
        a += 1
    if valor in ")":
        b += 1
if a == b:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está incorreta.")
print (a, b)