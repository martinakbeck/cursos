# Elabore um algoritmo que controle uma lista de itens de informática.
# Deverá ser exibido um menu com as seguintes opções:
# Adicionar, Listar, Excluir, Alterar e Sair.
# Adicionar somente poderá ser executado se o item já não exista
# Excluir somenta poderá ser executado se o item existir
# Alterar somenta poderá ser executado se o item existir, e deverá perguntar o novo nome do item (aplicar regra1)
# Deverá sempre exibir o menu novamente até que o usuário opte por SAIR
lista = []
op = 0


def cadastrar(pItem):
    produto = input('Informe nome do produto: ')
    if len(pLista) == 0:
        pLista.append(produto)
    else:
        for x in pLista:
            if (pLista[x] == produto):
                print('Produto já cadastrado')
            else:
                pLista.append(produto)

def listar():
    if (len(itens) == 0 ):
        return 'Não há itens cadastrados'
    return itens

def excluir(pLista):
    produto = input('Informe nome do produto: ')
    for x in pLista(0, len(pLista)):
        if (pLista[x] == produto):
            pLista[x].pop()
            print('Produto excluído')
        else:
            print('Produto não está na lista')

def alterar(pLista):
    produto = input('Informe nome do produto: ')
    for x in pLista(0, len(pLista)):
        if (pLista(x) == produto):
            pLista[x] = produto
            print('Produto alterado')
        else:
            print('Produto não existe na listagem')

def sair():
    return 'Seção encerrada'

def saudacao (pNome):
    return 'Olá ' + pNome + ', seja bem vindo!'

while (op != 5):
    op = int(input('Selecione uma função: \n'
    '1 - Adicionar \n'
    '2 - Listar \n'
    '3 - Excluir \n'
    '4 - Alterar \n'
    '5 - Sair \n'))
    if (op == 1):
        adicionar(lista)
    elif (op == 2):
        print(listar(lista))
    elif (op == 3):
        print(excluir(lista))
    elif (op == 4):
        print(alterar(lista))
    if (op == 5):
        print(sair())



