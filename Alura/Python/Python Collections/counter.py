from typing import DefaultDict


from collections import defaultdict

class Conta:
    def __init__(self):
        print('Criando um conta')

contas  = defaultdict(Conta)
contas[15]