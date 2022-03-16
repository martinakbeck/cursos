with open('cadastro.txt', 'w') as arquivo:
    arquivo.write('Escrevendo' + '\n')

with open('cadastro.txt', 'a') as arquivo:
    arquivo.write('Escrevendo 2')

with open('cadstro.txt', 'r') as arquivo:
    a = arquivo.readlines()
    print(a)
