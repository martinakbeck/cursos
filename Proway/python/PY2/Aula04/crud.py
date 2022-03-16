from classeConexao import Conexao
from time import sleep
import os


def montaCampos():
    global campos, valores
    opSair = 0
    campos = []
    while opSair != 0:
        campo = input('Informe o nome do Campo: ')
        campos.append(campo)
        opSair = int(input('Deseja informar mais um campo? 1-Sim | 0-Não'))

    valores = []
    for x in range(0, len(campos)):
        valor = input('Informe o valor para o campo ' + x +':')
        valores.append(valor)

    return campos, valores

def mostraMenu():
    opcao = 0
    while (opcao != 5):
        print('*-----------------------------*')
        print('| 1 - Cadastrar     2- Listar |')
        print('| 3 - Alterar      4- Excluir |')
        print('|         5 - Sair            |')
        print('*-----------------------------*')
        opcao = int(input('Digite a opção desejada: '))
        if ( opcao == 1 ):
            tabela = input('Informa nome da tabela: ')
            montaCampos()
            sleep(3)
            conexao.cadastra_dados(tabela, campos, valores)

        elif ( opcao == 2):
            tabela = input('Informa nome da tabela: ')
            montaCampos()
            conexao.retorna_valores(tabela, campos, valores)
            sleep(3)

        elif ( opcao == 3):
            tabela = input('Informa nome da tabela: ')
            montaCampos()
            clausula = input('Informe cláusula: ')
            conexao.alterar_dados(tabela, campos, valores, clausula)
            sleep(3)

        elif ( opcao == 4):
            tabela = input('Informa nome da tabela: ')
            clausula = input('Informe cláusula: ')
            conexao.excluir_dados(tabela, clausula)
            sleep(3)

        elif ( opcao == 5):
            print('Até mais')
            sleep(3)

        else:
            print('Opção inválida')
            sleep(3)
            os.system

conexao = Conexao('localhost', 'escola', 'root', '')

sleep(3)
os.system('cls')
conexao.retorna_login('cad_login')
mostraMenu()

# conexao = Conexao('localhost', 'escola', 'root', '')
# #conexao.retorna_dados('cad_alunos')
# #conexao.retorna_dados('cad_cursos')
# #alunos = ['Juca', 'm']
# #conexao.cadastra_dados('cad_alunos', 'nome_cad_aluno, sexo_cad_aluno', alunos)
# # valores = ['Jhonni', 'm']
# # campos = ['nome_cad_professor', 'sexo_cad_professor']
# # conexao.cadastra_dados('cad_professores', campos, valores)
# #conexao.retorna_dados('cad_professores')
# #conexao.excluir_dados('cad_alunos', 'id_cad_aluno = 1')

# # conexao.retorna_dados('cad_alunos')
# # conexao.aletar_dados('cad_alunos', 'nome_cad_aluno', 'Fabio', 'id_cad_aluno = 4' )
# # conexao.retorna_dados('cad_alunos')

# valor = (1)
# campo = ('id_cad_vendedor')
# conexao.retorna_total_registros('cad_vendedores', campo, valor)


