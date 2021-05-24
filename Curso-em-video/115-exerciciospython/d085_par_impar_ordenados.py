# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
temp = []
par = []
impar = []
lista = []
for c in range(0, 7):
    temp.append(int(input(f"Digite o {c + 1}º número: ")))
    if temp[0] % 2 == 0:
        par.append(temp[0])
    else:
        impar.append(temp[0])
    temp.clear()
par.sort()
impar.sort()    
lista.append(par[:])
lista.append(impar[:])
print(lista)
