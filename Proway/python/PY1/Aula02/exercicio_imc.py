for x in range(5):
    nome = input('Informe nome:')
    sexo = input('Informe sexo (F/M): ')
    peso = float(input('Informe peso: '))
    altura = float(input('Informe altura: '))

    abaixo_imc = 0
    normal_imc = 0
    obesidade_leve = 0
    obesidade_moderada = 0
    obesidade_mórbida = 0

    imc = peso/(altura**2)
    
    if ( sexo.upper() == 'F'):
        if imc < 19:
            abaixo_imc += 1
        elif imc >= 19 and imc <= 24.9:
            normal_imc += 1
        elif imc >= 24 and imc <=28.9:
            obesidade_leve += 1
        elif imc >= 29 and imc <= 38.9:
            obesidade_moderada += 1
        elif imc > 39:
            obesidade_mórbida += 1
    if ( sexo.upper() == 'M'):
        if imc < 20:
            abaixo_imc += 1
        elif imc >= 20 and imc <= 24.9:
            normal_imc += 1
        elif imc >= 25 and imc <=29.9:
            obesidade_leve += 1
        elif imc >= 30 and imc <= 39.9:
            obesidade_moderada += 1
        elif imc > 40:
            obesidade_mórbida += 1

print('Abaixo do peso: ' + str(abaixo_imc))
print('Normal: ' + str(normal_imc))
print('Obesidade Leve: ' + str(obesidade_leve))
print('Obesidade Moderado: ' + str(obesidade_moderada))
print('Abaixo do Mórbida: ' + str(obesidade_mórbida))

