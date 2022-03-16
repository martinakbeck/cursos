class Escritora:


    def __init__(self, nome_arquivo):
        self.file_name = nome_arquivo

    def escrever(self, produtos):
        with open(f'{self.file_name}.txt', 'a') as arquivo:
            arquivo.write(f'{produtos}' + '\n')

    def ler(self):
        with open(f'{self.file_name}.txt', 'r') as arquivo:
            conteudo = arquivo.readlines()
            print(conteudo)

    def produtos(self):
        contador = 5
        while contador > 0:
            id = int(input('ID: '))
            nome = (input('Nome: '))
            preco = float(input('Preço: '))
            produtos = (f'ID: {id}, Nome: {nome}, Preço: R${preco}')
            self.escrever(produtos)
            contador -= 1
            

criador_de_arquivo = Escritora('Cadastro')

criador_de_arquivo.produtos()

criador_de_arquivo.ler()





    