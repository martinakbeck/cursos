nome = input('Nome: ')
n1 = float(input('Informe primeira nota: '))
n2 = float(input('Informe segunda nota: '))
n3 = float(input('Informe terceira nota: '))
n4 = float(input('Informe quarta nota: '))

media = (n1 + n2 + n3 + n4)/4

if (media < 5):
    print('Média: %.2f | Reprovado' %media )
elif (media >= 5 and media <= 6.9):
    print('Média: %.2f | Em exame' %media )
else:
    print('Média: %.2f | Aprovado' %media )

