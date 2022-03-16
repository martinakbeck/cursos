# try:
#     comandos que deseja executar

# except:
#     mensagem de excessão
x = 0
try:
    print(2/0)
except NameError :
    print('Erro ao tentar dividir. Variável não declarada.')
except ZeroDivisionError :
    print('Erro ao tentar dividir. Não é possível dividir por zero.')
except:
    print('Erro genérico')
finally:
    # quando não quero que um erro que ocorreu não pare o sistema
    # ou trabalhar com uma rotina por debaixo dos panos
    print('Aqui continua normalmente')