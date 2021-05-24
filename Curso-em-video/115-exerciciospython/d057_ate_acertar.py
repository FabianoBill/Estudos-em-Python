# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Digite seu sexo [M/F]: ").strip()
while sexo not in "MF":
    sexo = input("Houve algum erro, digite novamente seu sexo [M/F]: ").strip()
print(f"Sexo {sexo} cadastrado. Obrigado.")