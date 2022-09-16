from documento import Documento
from telefones import TelefonesBr
from datas import DatasBr
from acesso_cep import BuscaEndereco
import re

CPF = '15316264754'
CNPJ = '35379838000112'
CEP = '01001000'
telefone = '556326481244'

doc = Documento.cria_documento(CPF)
print(doc)

padrao = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
texto = 'teste teste teste rodrigo123@gmail.com.br'
resposta = re.search(padrao, texto)
print(resposta.group())

telefone_obj = TelefonesBr(telefone)
print(telefone_obj)

cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())


cep_obj = BuscaEndereco(CEP)
print(cep_obj)
bairro, cidade, uf = cep_obj.acessa_via_cep()
print(bairro, cidade, uf)