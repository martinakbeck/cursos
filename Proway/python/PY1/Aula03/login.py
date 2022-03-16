def validaLogin(l, s):
    if ( s == 'proway' and l == 'aluno'):
        return 'Acesso liberado'
    else:
        return 'Acesso bloqueado'

login1 = input('Informe Login: ')
senha1 = input('Informe Senha: ')

print(validaLogin(login1, senha1))