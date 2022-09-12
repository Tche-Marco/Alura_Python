from datetime import date, timedelta
from datetime import datetime

data_atual = date.today()
print(data_atual)

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

data_e_hora_atuais = datetime.now()
data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto)

data_e_hora_em_string = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_string, '%d/%m/%Y %H:%M')
print(data_e_hora)

diferenca = timedelta()
print(diferenca)