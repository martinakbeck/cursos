from classeConexao import Conexao
from time import sleep
import os
# opcao = 0
# while (opcao != 5):
#     os.system('cls')
#     print('*-----------------------------*')
#     print('| 1 - Cadastrar     2- Listar |')
#     print('| 3 - Alterar      4- Excluir |')
#     print('|         5 - Sair            |')
#     print('*-----------------------------*')
#     opcao = int(input('Digite a opção desejada: '))
#     if ( opcao == 1 ):

#         sleep(3)

#     elif ( opcao == 2):
#         sleep(3)

#     elif ( opcao == 3):
#         sleep(3)

#     elif ( opcao == 4):
#         sleep(3)

#     elif ( opcao == 5):
#         sleep(3)



conexao = Conexao('localhost', 'escola', 'root', '')
#conexao.retorna_dados('cad_alunos')
#conexao.retorna_dados('cad_cursos')
#alunos = ['Juca', 'm']
#conexao.cadastra_dados('cad_alunos', 'nome_cad_aluno, sexo_cad_aluno', alunos)
# valores = ['Jhonni', 'm']
# campos = ['nome_cad_professor', 'sexo_cad_professor']
# conexao.cadastra_dados('cad_professores', campos, valores)
#conexao.retorna_dados('cad_professores')
#conexao.excluir_dados('cad_alunos', 'id_cad_aluno = 1')

# conexao.retorna_dados('cad_alunos')
# conexao.aletar_dados('cad_alunos', 'nome_cad_aluno', 'Fabio', 'id_cad_aluno = 4' )
# conexao.retorna_dados('cad_alunos')

valor = (1)
campo = ('id_cad_vendedor')
conexao.retorna_total_registros('cad_vendedores', campo, valor)


