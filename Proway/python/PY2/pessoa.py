nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))



class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        self.cabecalho()
        print(f'Meu nome é {self.nome} tenho {self.idade} anos e {self.altura} de altura')
        self.rodape()

    def cabecalho(self):
        print('*'*30)

    def rodape(self):
        print('='*30)
        
        

eu = Pessoa(nome, idade, altura)
eu.apresentar()

