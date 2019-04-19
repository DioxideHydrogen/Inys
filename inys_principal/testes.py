nome_alarme = raw_input('Digite o nome do alarme: ')
frase = 'Digite o dia do evento'
data_alarme = raw_input('Digite o dia: ')
hora_alarme = raw_input('Digite a hora: ')
sql = 'INSERT INTO alexa_alarmes(nome, data, hora) VALUES (%s, %s, %s)',(nome_alarme, data_alarme, hora_alarme)
print type(sql)
sql = sql[0]
print type(sql)
print ''+str(sql)+''