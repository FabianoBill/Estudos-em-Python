def ola_mundo():
    return "Olá mundo"
print(ola_mundo())
print(type(ola_mundo))

def nada():
    pass
print(nada())
resultado = nada()
print(type(resultado))

def ola(nome, sobrenome=" ", idade=0):           # o = torna o parametro opcional no caso espaço é o default
    return f'Olá {nome} {sobrenome} com {idade} anos.'
print(ola("Fabiano", "Bill", 45))
print(ola("Fabiano", idade=45, sobrenome="Bill"))
print("===tupla variáve===")
def soma(*args):                # l
    print(args)
    print(type(args))
    ac = 0
    for valor in args:
        ac += valor
    return ac
a = soma()
print(a)
b = soma(1, 2, 3)
print(b)
print("===dicionário variável===")
def dic(**kwargs):              #
    print(kwargs)
dic(nome="Fabiano", idade=45)
print("===tupla e dicionário===")
def mix(*args, **kwargs):       #
    print(args)
    print(kwargs)
mix(0, 1, 2, nome="Bill", idade=45)
a = (1, 2, 3)
b = {'nome':"Bill", 'sobrenome':"Jaba"}

mix(a, b)
mix(*a, **b)


