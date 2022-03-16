aparicoes = {
    'Guilherme' : 1,
    'cachorro' : 2,
    'nome' : 2,
    'vindo': 1
}

aparicoes['Carlos'] = 2

print(aparicoes)

del aparicoes['Carlos']

print(aparicoes)

print('cachorro' in aparicoes)

#passar pelas chaves
for elemento in aparicoes.keys():
    print(elemento)

#passar pelos valores
for elemento in aparicoes.values():
    print(elemento)

#passar pela "duplinha"
for elemento in aparicoes:
    print(elemento, aparicoes[elemento])
for elemento in aparicoes.items():
    print(elemento)


    
