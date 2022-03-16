from sqlite3 import sqlite_version
import mysql.connector

class Conexao():


    _MSG_MENSAGEM_CLAUSULA_DELETE = 'Necessário informar o registro que deseja excluir'
    _MSG_MENSAGEM_CLAUSULA_UPDATE = 'Necessário informar o registro que deseja alterar'
    _MSG_SUCESSO_EXCLUIR = 'Registro excluido com sucesso'
    _MSG_SUCESSO_ALTERAR = 'Registro alterado com sucesso'
    _MSG_SUCESSO_INSERIR = 'Registro inserido com sucesso'
    _MSG_ERRO_EXCLUIR = 'Erro ao excluir o registro'
    _MSG_ERRO_ALTERAR = 'Erro ao alterar o registro'
    _MSG_ERRO_INSERIR = 'Erro ao inserir o registro'
    _MSG_REGISTRO_INEXISTENTE = 'Registro inexistente'

    def __init__(self, host, banco, usuario, senha):
        self.host = host
        self.database = banco
        self.user = usuario
        self.password = senha
        self.conn = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        if self.conn.is_connected():
            print ('Conexão efetuada com sucesso')
        else:
            print('Falha na conexão ao banco/servidor')

    
    
    
    
    
    
    
    
    
    
    def retorna_dados(self, tabela, campos, clausula = ''):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            sql = 'SELECT '
            sqlC = ''
            for x in range(0, len(campos)):
                sqlC += campos[x] + ', '
            sqlC = sqlC[:-2]
            sql += sqlC + ' FROM ' + tabela
            if clausula != '':
                sql += ' WHERE ' + clausula
            cursor.execute(sql)
            linha = cursor.fetchall()
            if ( cursor.rowcount == 0):
                print('Não foram encontrados registros com a seleção atual. [Tabela = ' + tabela + ']')
            else:
                print('Resultado da consulta [Tabela = ' + tabela + ']')
            if len(campos) == 1:
                for reg in linha:
                    print(reg[x])
            else:
                registros = ''
                for x in range (0, len(campos)-1):                        
                    for reg in linha:
                        registros += str(reg[x]) + ' | '
                print(registros)
            print('Total de Registros: ' + str(cursor.rowcount))

            # if clausula != '':
            #     cursor.execute('SELECT * FROM ' + tabela + ' WHERE ' + clausula)
            # else:
            #     cursor.execute('SELECT * FROM ' + tabela)
            # #one - 1 registro | all - todos
            # linha = cursor.fetchall()
            # if ( cursor.rowcount == 0 ):
            #     print('Não foram encotrados registros com a seleção atual')
            # else:
            #     print('Resultado da consulta')


                # for reg in linha:
                #     if reg[2] == 'f':
                #         print(str(reg[0]) + ' | ' + reg[1] + ' | Feminino')
                #     else:
                #         if reg[2] == 'm':
                #             print(str(reg[0]) + ' | ' + reg[1] + ' | Masculino')
                #         else:
                #             print(str(reg[0]) + ' | ' + reg[1] + ' | Sexo Inválido')
#                    elif reg[2] == 'm':
#                        print(str(reg[0]) + ' | ' + reg[1] + ' | Masculino')
#                    else:
#                        print(str(reg[0]) + ' | ' + reg[1] + ' | Indefinido')
            print('Total de Registros: ' + str(cursor.rowcount))

    def cadastra_dados(self, tabela, campos, valores):
        if self.conn.is_connected():

            sql = 'INSERT INTO ' + tabela + ' ('
            sqlC= ''
            for x in range (0, len(campos)):
                sqlC += campos[x] + ', '
            sqlC = sqlC[:-2]
            sql += sqlC + ') VALUES ('
            sqlV = ''
            for x  in range(0, len(valores)):
                if ( type(valores[x]) is int) or (type(valores[x]) is float):
                    sqlV += '' + str(valores [x]) + ', '
                else:
                    sqlV += '"' + str(valores [x]) + '", '
            sqlV = sqlV[:-2]
            sql += sqlV + ')'
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql)
                print(self._MSG_SUCESSO_INSERIR)
                self.conn.commit()
            except:
                self.conn.rollback()
                print(self._MSG_ERRO_INSERIR)
        

        # sql = 'INSERT INTO ' + tabela + ' (' + campos + ') VALUES ("' + valores[0] + '", "' + valores[1] + '")'
        # print(sql)
        # if self.conn.is_connected():
        #     cursor = self.conn.cursor()
        #     try:
        #         cursor.execute('INSERT INTO ' + tabela + ' (' + campos + ') VALUES ("' + valores[0] + '", "' + valores[1] + '")')
        #         self.conn.commit()
        #         print(self._MSG_SUCESSO_INSERIR)
        #     except:
        #         self.conn.rollback()
        #         print(self._MSG_ERRO_INSERIR)

    def excluir_dados(self, tabela, clausula):
        if self.conn.is_connected():
            if clausula == '':
                print(self._MSG_MENSAGEM_CLAUSULA_DELETE)
            else:
                if not (self.retorna_total_registros(tabela, clausula)):
                    try:
                        cursor = self.conn.cursor()
                        cursor.execute('DELETE FROM ' + tabela + ' WHERE ' + clausula)
                        self.conn.commit()
                        print(self._MSG_SUCESSO_EXCLUIR)
                    except:
                        self.conn.rollback()
                        print(self._MSG_ERRO_EXCLUIR)
        # if clausula == '':
        #     print(self._MSG_MENSAGEM_CLAUSULA_DELETE)
        # else:
        #     if self.conn.is_connected():
        #         try:
        #             cursor = self.conn.cursor()
        #             cursor.execute('DELETE FROM ' + tabela + ' WHERE ' + clausula)
        #             self.conn.commit()
        #             print(self._MSG_SUCESSO_EXCLUIR)
        #         except:
        #             self.conn.rollback()
        #             print(self._MSG_ERRO_EXCLUIR)

    def aletar_dados(self, tabela, campos, valores, clausula):
         if self.conn.is_connected():
            if clausula == '':
                print(self._MSG_MENSAGEM_CLAUSULA_UPDATE)
            else:
                if self.retorna_total_registros(tabela, clausula):
                    cursor = self.conn.cursor()
                    sql = 'UPDATE ' + tabela
                    sqlC = ' SET '
                    for x in range (0, len(campos)):
                        if ( (type(valores[x] is int)) or (type(valores[x] is float))):                            
                            sqlC = campos[x] + ' = ' + str(valores[x]) + ', '
                        else:
                            sqlC = campos[x] + ' = "' + str(valores[x]) + '", '
                    sql += sqlC + ' WHERE ' + clausula
                    try:
                        cursor = self.conn.cursor()
                        cursor.execute(sql)
                        self.conn.commit()
                        print(self._MSG_SUCESSO_ALTERAR)
                    except:
                        self.conn.rollback()
                        print(self._MSG_ERRO_ALTERAR)

     
       
        # if clausula == '':
        #     print(self._MSG_MENSAGEM_CLAUSULA_ALTERAR)
        # if self.conn.is_connected():
        #     try:
        #         cursor = self.conn.cursor()
        #         cursor.execute('UPDATE ' + tabela + ' SET ' + campo + ' = "' + valor + '" WHERE '  + clausula)
        #         self.conn.commit()
        #         print(self._MSG_SUCESSO_ALTERAR)
        #     except:
        #         self.conn.rollback()
        #         print(self._MSG_ERRO_ALTERAR)

    def retorna_total_registros(self, tabela, clausula = '1 = 1'):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            sql = 'SELECT * FROM ' + tabela + ' WHERE ' + clausula
            cursor.execute(sql)            
            linha = cursor.fetchall()
            if (cursor.rowcount == 0):
                print(self._MSG_REGISTRO_INEXISTENTE)
                return False
            return True


