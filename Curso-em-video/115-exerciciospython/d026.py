f = input('Escreva uma frase: ').lower().strip()
print('A letra (a) aparece {} vezes na frase.'.format(f.count('a')))
print('A letra (a) aparece pela primeira vez na posição: ', f.find('a')+1)
print('A letra (a) aparece pela última vez na posição: ', f.rfind('a')+1)
