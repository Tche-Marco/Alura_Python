from documento import Documento
from telefones import TelefonesBr
from datas import DatasBr
from acesso_cep import BuscaEndereco
import re

cpf = '15316264754'
cnpj = '35379838000112'

doc = Documento.cria_documento(cpf)
print(doc)

padrao = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
texto = 'aaabbbbbbxxx rodrigo123@gmail.com.br'
resposta = re.search(padrao, texto)
print(resposta.group())

telefone = '556326481244'
telefone_obj = TelefonesBr(telefone)

print(telefone_obj)

cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())

cep = 77015770
cep_obj = BuscaEndereco(cep)
print(cep_obj)
