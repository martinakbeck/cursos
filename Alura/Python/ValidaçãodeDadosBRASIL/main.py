from datetime import date
from Cpf_cnpj import Documento
from validate_docbr import CNPJ
from TelefonesBr import TelefonesBr
import re
from datas_br import DatasBR
from acesso_cep import BuscaEndereco
import requests

exemplo_cnpj = '35379838000112'
exemplo_cpf = '07449433966'
documento = Documento.criar_documento(exemplo_cpf)
print(documento)

telefone = '552136431234'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

cadastro = DatasBR()
print(cadastro.mes_cadastro())
print(cadastro)

hoje = DatasBR()
print(hoje.tempo_cadastro())

cep = 89063002
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

bairro, cidade, uf = objeto_cep.acessa_viacep()
print(bairro, cidade, uf)
