class Animal:
    def __init__(self, patas, calda, som):
        self.patas = patas
        self.calda = calda
        self.som = som

    def emitir_som(self):
        print(self.som)


class Cachorro(Animal):

    def nadar(self):
        print('Sou um cachorro e estou nadando')


class Cobra(Animal):

    def subir_arvores(self):
        print('Sou uma cobra e estou subindo em arvore')

cachorro = Cachorro(patas= 4, calda=True, som='Au au au')

cachorro.emitir_som()
cachorro.nadar()

cobra = Cobra(patas= 8, calda=True, som='ZZZzzzZZZ')

cobra.emitir_som()
cobra.subir_arvores()