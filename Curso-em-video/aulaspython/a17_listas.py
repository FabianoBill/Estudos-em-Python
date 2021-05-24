# Listas
n = [3, 5 ,8, 1, 2]
print(n)
n[2] = 0 # troca o elemento 8 pelo zero
print(n)
n.append(7) # acrescenta no final
print(n)
n.sort() # ordena
print(n)
n.sort(reverse=True) # ordena invertido
print(n)
n.insert(2, 9) # insere (posição, valor)
print(n)
n.pop(2) # exclui o elemento da posição indicada (vasio exclui o último)
print(n)
n.remove(1)
print(n)
for pos, valor in enumerate(n):
    print(f"Na posição {pos} temos o valor {valor}.")

a = [2, 4, 9, 1]
b = a    # ocorre uma ligação
b[0] = 5 # ambas as listas irão mudar
print(a)
print(b)

a = [2, 4, 9, 1]
b = a[:]  # assim b copia os valores de a e não ocorre a ligação
b[0] = 5 # apenas b irá mudar
print(a)
print(b)