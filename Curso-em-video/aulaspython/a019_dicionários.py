pessoas = {"nome": "Fabiano", "sexo": "M", "idade": 44}
print(pessoas["nome"])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(k, v)

    # Inserindo um dicionário em uma lista
# estado = {}
# brasil = []
# for c in range(0, 3):
#     #estado.append(input("Nome: "))   --> não funciona
#     estado["nome"] = input("Nome: ")
#     estado["UF"] = input("UF: ")
#     estado["pop"] = int(input("Populaçao: "))
#     brasil.append(estado.copy())
# print(brasil)

    # Inserindo uma lista em um dicionário 
# estado = []
# brasil = {}
# for c in range(0, 3):
#     # a[c] = input("Nome: ")  --> não funciona
#     estado.append(input("Nome: "))
#     estado.append(input("UF: "))
#     estado. append(int(input("Populção: ")))
#     brasil[f'estado {c}'] = estado[:]
#     estado.clear()
# print(brasil)

# from operator import itemgetter
# n = {"n1": 3, "n2": 5, "n3": 1}
# v = []
# v = sorted(n.items(), key=itemgetter(1))
# print(v)