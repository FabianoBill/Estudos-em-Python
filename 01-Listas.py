print("###Listas###")
lista = list(range(10))
print(lista)
print(list(range(10, 0, -1)))
print(dir(list))
lista.sort()  #ordena
lista.append(10) #adciona último
print(lista)
lista.pop() #remove último
print(lista)
lista.extend([10, 11])
print(lista)
print(lista + [12, 13, 14])
print(lista*2)
nome = "Fabiano Bill"
print('*'.join(nome))
print(nome.split())
nome = "Fabiano-Bill"
nome = nome.split('-')
print(nome)
print('*'.join(nome))


