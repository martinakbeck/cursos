valor = int(input('Informe valor para tabuada: '))
print('Tabuada')
for x in range (1,11,1):
    print(str(x) + ' x ' + str(valor) + ' = ' + str(x*valor) )

#decrescente
print('Ordem decrescente')
for x in range(10,0,-1):
    print(x)