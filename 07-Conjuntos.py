conjunto1 = {1, 3, 7, 0, 5}
print(conjunto1, type(conjunto1))
conjunto2 = {1, 1, 2, 2, 2}
print(conjunto2)
conjunto1.add(4)
print(conjunto1)
conjunto1.discard(1)
print(conjunto1)
conjunto1 = {1, 3, 7, 0, 5}
conjunto2 = {1, 1, 2, 2, 2}
uniao = conjunto1.union(conjunto2)
print(1, uniao)
intercecao = conjunto1.intersection(conjunto2)
print(2, intercecao)
diferenca = conjunto1.difference(conjunto2)
print(3, diferenca)
diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(4, diferenca_simetrica)
A = {1, 2}
B = {1, 2, 3, 4}
print(5, A.issubset(B))
print(6, B.issubset(A))
print(7, B.issuperset(A))