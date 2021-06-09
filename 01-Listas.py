print("###Listas###")
lista = list(range(10))
print(1, lista)
print(2, list(range(10, 0, -1)))
print(3, dir(list))
print(4, lista.sort())  #ordena
print(4.1, lista)
print(5, lista.append(10))  #adciona último
lista.append(11)
print(5.1, lista)
print(6, lista.pop())  #remove último
lista.pop()
print(6.1, lista)
print(7, lista.extend([11, 12]))
print(7.1, lista)
print(8, lista + [13, 14, 15])
print(9, lista*2)
nome = "Fabiano Bill"
print(10, '*'.join(nome))
print(11, nome.split())
nome = "Fabiano-Bill"
print(12, nome.split('-'))
print(13, '*'.join(nome))

numeros = [2, 1, 3, 5, 8]
animais = ['gato', 'burro', 'arara', 'lobo']

numeros.pop(0)
print(14, numeros)
animais.pop(0)
print(15, animais)
animais.append('boi')
animais.remove('burro')
print(animais)
animais.sort()
print(animais)
animais.reverse()
print(animais)