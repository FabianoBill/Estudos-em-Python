# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

n = (int(input("Digite um número: ")), int(input("Digite um número: "))
    , int(input("Digite um número: ")), int(input("Digite um número: ")))
print(f"O número 9 apareceu {n.count(9)} vezes.")
if 3 in n:
    print(f"O numero 3 apareceu na {n.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado.")
print("Os números pares digitados foram: ", end="")
for c in n:
    if c % 2 == 0:
        print(f"{c} ", end="")
