print("###Tuplas###")
print(tuple(range(5)))
t = (5, 6, 7)
print(type(t))
print(t[::-1])
t = (5)
print(type(t)) # não reconhece uma tupla e sim um inteiro numa ordem de procedência
t = (5,)
print(type(t)) # aí sim uma tupla de um elemento
registro = ("Bill", 45)
nome, idade = registro #Desempacotamento
print(nome)
print(idade)
registro2 = ("Fabiano", 44)
r = registro + registro2
print(r)                #É uma nova tupla pois tuplas são imutáveis
print(id(registro))
print(id(registro2))
print(id(r))            # são números diferentes, logo, tuplas diferentes


