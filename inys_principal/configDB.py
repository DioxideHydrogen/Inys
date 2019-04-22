# -*- coding : utf-8 -*-

#	Arquivo de configuracoes da Database
#	Estao sujeitos a mudanca as variaveis:
#	host, user, password, banco e porta 
#	Modifiqueas conforme seu sistema
 
 
class configs():
	def credentialsDB(x):
		host = 'localhost'
		user = '' #Usuario da database 
		password = '' #Senha da sua database 
		banco = 'alexa_db' #Nome do banco de dados (Homenagem a Alexa da Amazon) **Nao trocar**
		porta = 3306 #Porta utilizada pelo servico MySQL
		creds = [host, user, password, banco, porta]
		return creds;
