import mysql.connector

#host, database, usuario, senha
con = mysql.connector.connect(host='localhost', database='escola',user='root', password='')

if con.is_connected():
    print('Conexão efetuada com sucesso')
else:
    print('Erro na conexão com o banco de dados/servidor')