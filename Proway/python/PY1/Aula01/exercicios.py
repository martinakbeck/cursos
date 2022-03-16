v1 = int(input("Informe um valor: "))
v2 = int(input("Informe outro valor: "))
if (v1 == v2):
    print('Valores precisam ser diferentes')
else:
    v3 = int(input("Informe mais um valor: "))
    if (v1 == v3 or v3 == v2):
        print('Valroes precisam ser diferentes')
    else:
        if ( v1 == v2 or v2 == v3 or v1 == v3):
            print('Os valores devem ser diferentes')
        elif (v1 < v2 and v1 < v3):
            if (v2 < v3):
                print(f'{v1}, {v2}, {v3}')
            else:
                print(f'{v1}, {v3}, {v2}')
        elif (v2 < v1 and v2 < v3):
            if (v1 < v3):
                print(f'{v2}, {v1}, {v3}')
            else:
                print(f'{v2}, {v3}, {v1}')
        elif (v3 < v1 and v3 < v2):
            if (v1 < v2):
                print(f'{v3}, {v1}, {v2}')
            else:
                print(f'{v3}, {v2}, {v1}')