
linguas = {'BR': "Português", 'EUA': "Inglês"}
print(linguas['BR'])
print(linguas.get('EUA'))
print('BR' in linguas)
linguas['ES'] = "Espanhol"
print(linguas)
for chave in linguas.keys():
    print(chave)
for valor in linguas.values():
    print(valor)
for chave, valor in linguas.items():
    print(chave, valor)
linguas.pop('BR')
print(linguas)
del linguas['EUA']
print(linguas)

