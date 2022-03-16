class Categoria:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    

class Produto(Categoria):
    def __init__(self, nome, preco, categoria):
        super().__init__(nome, preco, categoria)

    def cadastro(self):
        print(f'{self.nome}, R$ {self.preco}, categoria {self.categoria}')


produto = Produto(nome= 'Caixa de Sabão em pé', preco=17.80, categoria='limpeza').cadastro()