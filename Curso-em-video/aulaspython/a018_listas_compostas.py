pessoas = []
dados = []
for c in range(0, 3): # monta uma lista dentro da outra
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados)
    dados.clear()

print(pessoas)
