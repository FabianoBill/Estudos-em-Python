class Pessoa:
    olhos = 2                                               # atributo default ou atributo de classe
    def __init__(self, nome=None, idade=0, *filhos):     # metodo construtor (alt+enter cria o atributo)
        self.filhos = list(filhos)                         # atributos de dados (field)
        self.idade = idade
        self.nome = nome

    def metodo(self):                                   # atribudo de método
        return f"olá {id(self)}"
    @staticmethod                                       # método de classe ou estático
    def metodo_estatico():
        return 45
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} - olhos {cls.olhos}"

fabiano = Pessoa("Fabiano", 45)
flavia = Pessoa("Flavia", 42)
coutinho = Pessoa("Coutinho", 80, fabiano, flavia)
print(1, fabiano.metodo(), fabiano.nome, fabiano.idade, fabiano.filhos)
print(2, coutinho.nome, coutinho.idade)
print(fabiano.__dict__)
print(flavia.__dict__)
print(coutinho.__dict__)
for filho in coutinho.filhos:
    print(3, filho.nome)
print(Pessoa.nome_e_atributos_de_classe(), fabiano.nome_e_atributos_de_classe())
