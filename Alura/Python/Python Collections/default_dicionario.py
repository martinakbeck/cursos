from collections import defaultdict, Counter

meu_texto = 'Bem vindo meu nome é Martina eu gosto muito de nomes e tneho o meu cachorro e gosto muito de cachorro'
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra,0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes = {}

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

aparicoes = Counter(meu_texto.split())

print(aparicoes)
