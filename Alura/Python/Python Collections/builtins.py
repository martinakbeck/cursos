idades = [15, 87, 32, 65, 56, 32, 49 ,37]

for i in range(len(idades)):
    print (i, idades[i])


for valor in enumerate(idades):
    print(valor)

for indice, valor in enumerate(idades):
    print(indice, valor)

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39, 1979),
]

for nome, idade, nascimento in usuarios:
    print(nome)

for nome, _, _ in usuarios:
    print(nome)

print(sorted(idades))
print(reversed(idades))