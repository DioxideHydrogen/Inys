# -*- coding: utf8 -*-
from datetime import date 
from datetime import datetime
from time import sleep
import tkinter as tk
from tkinter import ttk
import subprocess
from playsound import playsound
import platform

so = platform.system()

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
def popupmsg(msg):
    cmd = ['xterm']
    cmd.extend(['-e', 'python tocarAlarme.py; exec $SHELL' ])
    subprocess.Popen(cmd, stdout=subprocess.PIPE)
    popup = tk.Tk()
    popup.wm_title("Alarme")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
while True:
	if so == 'Linux':
		import MySQLdb
		host = 'localhost'
		user = 'alexa_login'
		password = '19862010'
		banco = 'alexa_db'
		porta = 3306

		con = MySQLdb.connect(host,user,password,banco,porta)
		c = con.cursor(MySQLdb.cursors.DictCursor)

		def select(query):
			global c
			#query = "SELECT " + colunas + " FROM " + tabelas
			#if where:
			#	query += " WHERE " + where
			c.execute(query)
			return c.fetchall()
		def delete(query, sql_data):
			try:
				global c,con 
				#query = "DELETE FROM " + tabela + " WHERE " + where
				c.execute(query, sql_data)
				#con.commit()
			except (AttributeError, MySQLdb.OperationalError):
				c.execute(query, sql_data)

		x = select('SELECT * FROM alexa_alarmes') #Seleciona todos os alarmes da database da alexa
		alarmes = len(x)
		print '                          \033[33mAlarmes\033[0;0m \033[31mconfigurados:\033[0;0m \033[32m\033[1m'+ str(len(x))+'\033[0;0m'
		i = 0
		while i < alarmes:
			con = MySQLdb.connect(host,user,password,banco,porta)
			c = con.cursor(MySQLdb.cursors.DictCursor)
			hoje = date.today()
			hora = datetime.now()
			if so == 'Linux':
				dataAtual = str(hoje.day)+'/'+str(hoje.month)+'/'+str(hoje.year)
				horaAtual = str(hora.hour)+':'+str(hora.minute)

				print '''
				 	     \033[33mAlexa\033[0;0m \033[31mAlarme\033[0;0m \033[32m\033[1mv0.2\033[0;0m
				 	     \033[33mHora\033[0;0m \033[31matual:\033[0;0m \033[32m\033[1m{}\033[0;0m
				 	     \033[33mData\033[0;0m \033[31matual:\033[0;0m \033[32m\033[1m{}\033[0;0m
				\033[47m\033[30m=======================================\033[0;0m'''.format(horaAtual, dataAtual)
				print '                             Alarme: '+ str(i)
				tupla = x[i]
				idAlarme = tupla['id_alarmes']
				dataAlarme = tupla['data']
				print '                       Data do Alarme: ' + dataAlarme
				horaAlarme = tupla['hora']
				print '                       Hora do Alarme: ' + horaAlarme
				nomeAlarme = tupla['nome']
				print '                       Nome do Alarme: ' + nomeAlarme
				print '''
				\033[47m\033[30m=======================================\033[0;0m'''
				if dataAlarme == dataAtual and horaAlarme == horaAtual:
					popupmsg('Alarme: '+nomeAlarme+', hoje, dia: '+dataAlarme+' ás: '+horaAlarme+'!')
					import database
					deleteAlarme = "DELETE FROM alexa_alarmes WHERE id_alarmes={}".format(idAlarme)
					try:
						database.delete(deleteAlarme)
					except Exception as err:
						print err
				i = i+1
				sleep(5)
			elif so == 'Windows':
				print '''
					======================================='''
				print 'Alarme: '+ str(i)
				tupla = x[i]
				idAlarme = tupla['id_alarmes']
				dataAlarme = tupla['data']
				print 'Data do Alarme: ' + dataAlarme
				horaAlarme = tupla['hora']
				print 'Hora do Alarme: ' + horaAlarme
				nomeAlarme = tupla['nome']
				print 'Nome do Alarme: ' + nomeAlarme
				hoje = date.today()
				hora = datetime.now()
				dataAtual = str(hoje.day)+'/'+str(hoje.month)+'/'+str(hoje.year)
				print 'Data atual: ' + dataAtual
				horaAtual = str(hora.hour)+':'+str(hora.minute)
				print 'Hora atual: ' + horaAtual
				print '''
				======================================='''
				if dataAlarme == dataAtual and horaAlarme == horaAtual:
					import database
					query = "DELETE FROM alexa_alarmes WHERE id_alarmes={}".format(idAlarme)
					database.delete(query)
					popupmsg('Alarme: '+nomeAlarme+', hoje, dia: '+dataAlarme+' ás: '+horaAlarme+'!')
				i = i+1
				sleep(5)
			else:
				print '[!2ALR!] Sistema Operacional Não Identificado.'