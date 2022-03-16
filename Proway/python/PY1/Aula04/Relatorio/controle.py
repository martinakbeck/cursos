# Exercicio - Elabore um algoritmo para manipular arquivos em listas.
# Deverá ter opções de cadastro | alteração | visualização | exclusão | Carregar log | Carregar Informações
# Cada vez que selecionar uma das opções, deverá adiconar a respectiva ação em um arquivo log.txt
# Também deverá ter uma opção para 'exportar' as informações, que será gerada em um arquivo dados.txt
from funcoes import listar, cadastrar, excluir2, alterar, gravaLogDados, lerArquivo
itens = []
opcao = 0
while ( ( opcao >= 1 ) or ( opcao <= 5 ) ) :
    opcao = int(input('Selecione a opção desejada: \n' + 
                    '1- Listar           2- Cadastrar \n' + 
                    '3- Excluir          4- Alterar \n' +
                    '5- Exportar Dados   6- Carregar Log\n' + 
                    '7- Carregar Dados   8 - Sair     \n' +
                    '-----------------------------\n' ))  
    if ( opcao == 1 ):
        print(listar(itens))
    elif ( opcao == 2 ):
        item = input('Informe o nome do item para cadastrar: ')
        print(cadastrar(item, itens))
    elif ( opcao == 3 ):
        item = input('Informe o nome do item para excluir: ')        
        print(excluir2(item, itens))
    elif ( opcao == 4 ):
        if ( len(itens) == 0 ):
            print('A lista está vazia')
        else:
            item = input('Informe o nome do item que deseja alterar: ')
            print(alterar(item, itens))
    elif ( opcao == 5 ):
        if ( len(itens) > 0):
            gravaLogDados('Dados cadastrados\n' + itens + str('\n'), 2)
        else:
            print('Lista Vazia')
    elif ( opcao == 6 ):
        lerArquivo(1)
    elif ( opcao == 7 ):
        lerArquivo(2)
    elif ( opcao == 8 ):
        break
    else:
        print('Opção inválida')