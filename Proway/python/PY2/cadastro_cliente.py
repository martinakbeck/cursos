class CadastroPessoa:
    def __init__(self, nome, cliente_vip):
        self.nome = nome
        self.cliente_vip = cliente_vip

class Cliente(CadastroPessoa):

    def eh_vip(self):
        if self.cliente_vip == True:
            print(f'{self.nome} é cliente VIP!')
        else:
            print(f'{self.nome} não é cliente VIP!')

junior = Cliente('Júnior', cliente_vip=True)
junior.eh_vip()
ana = Cliente('Ana', cliente_vip=False)
ana.eh_vip()