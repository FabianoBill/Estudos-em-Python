# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

cadastro = {}
cadastro["nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
cadastro["Idade"] = date.today().year - nasc
cadastro["ctps"] = input("CTPS nº: (0 não tem) ")


if cadastro["ctps"] not in "0":
    cadastro["cont"] = int(input("Ano de contratação: "))
    cadastro["sal"] = float(input("Salário: "))
    cadastro["apos"] = date.today().year - cadastro["cont"] + 30
for k, v in cadastro.items():
    print(f"{k}: {v}")

