class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print (f'Meu nome é {self.nome} tenho {self.idade} anos e {self.altura} de altura')


pablo = Pessoa('Pablo', 20, 1.60)

pablo.apresentar()

print(pablo.nome)
print(pablo.altura)
print(pablo.idade)




