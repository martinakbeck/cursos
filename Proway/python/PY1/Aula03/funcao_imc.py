def retornaIMC(pAltura, pPeso):
    imc = pPeso/(pAltura**2)
    return imc

def imc_f(pIMC):
    if pIMC < 19:
        return 'Abaixo do pPeso'
    elif pIMC >= 19 and pIMC <= 24.9:
        return 'Normal'
    elif pIMC >= 24 and pIMC <=28.9:
        return 'Obesidade Leve'
    elif pIMC >= 29 and pIMC <= 38.9:
        return 'Obesidade Moderada'
    elif pIMC > 39:
        return 'Obesidade Mórbida'

def imc_m(pIMC):
    if pIMC < 20:
        return 'Abaixo do peso'
    elif pIMC >= 20 and pIMC <= 24.9:
        return 'Normal'
    elif pIMC >= 25 and pIMC <=29.9:
        return 'Obesidade Leve'
    elif pIMC >= 30 and pIMC <= 39.9:
        return 'Obesidade Moderada'
    elif pIMC > 40:
        return 'Obesidade Mórbida'
          
nome = input('Informe nome:')
sexo = input('Informe sexo (F/M): ')
peso = float(input('Informe peso: '))
altura = float(input('Informe altura: '))

imc = retornaIMC(altura, peso)
if (sexo.upper() == 'F'):
    print(imc_f(imc))
elif(( sexo.upper() == 'M')):
    print(imc_m(imc))
else:
    print('Opção Inválida')
