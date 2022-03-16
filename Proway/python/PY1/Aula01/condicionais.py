v1 = int(input("Informe um valor: "))
v2 = int(input("Informe outro valor: "))
v3 = int(input("Informe outro valor: "))

if (v1 >= v2 and v1 >= v3):
    print(f'{v1} é maior.')
elif (v2 >= v3 and v2 >= v1):
    print(f'{v2} é maior.')
elif (v3 >= v2 and v3 >= v1):
    print(f'{v3} é maior.')
elif (v1 == v2 and v2 == v3 and v1 == v3):
    print('Valores iguais')