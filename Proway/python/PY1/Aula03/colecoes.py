#list
valores = [1, 2, 3]
print(type(valores))
valores.append('teste')
print(valores)
valores.append(False)
print(valores)
valores[1] = 6
print(valores)
valores.pop(1)
print(valores)
print(len(valores))
for x in range(0,len(valores)):
    print(valores[x])


#tuple
#valores = (1, 2, 3)
#print(type(valores))

#valores2 = (1,'2', True, 10.4)
#print(type(valores2))
#print(valores2[1])

#meses = ('Jan', 'Fev', 'Mar')
#print(meses)
#for m in range (0, len(meses)):
#    print(str(m+1) + ' - ' + meses[m])

