class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_martina = ContaCorrente(15)
conta_martina.deposita(500)
print(conta_martina)

conta_dani = ContaCorrente(47685)
conta_dani.deposita(1000)

contas = [conta_martina, conta_dani]

print(contas)