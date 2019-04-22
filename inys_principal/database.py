import MySQLdb
from configDB import *

data = configs()
creds = data.credentialsDB()

host = creds[0]
user = creds[1]
password = creds[2]
banco = creds[3]
porta = creds[4]

con = MySQLdb.connect(host,user,password,banco,porta)
c = con.cursor(MySQLdb.cursors.DictCursor)


def connect():
	host = creds[0]
	user = creds[1]
	password = creds[2]
	banco = creds[3]
	porta = creds[4]

	con = MySQLdb.connect(host,user,password,banco,porta)
	c = con.cursor(MySQLdb.cursors.DictCursor)
	return c

def select(query):
	try:
		global c
		c.execute(query)
		return c.fetchall()
	except (AttributeError, MySQLdb.OperationalError):
		c = connect()
		c.execute(query)
		return c.fetchall()
def insert(sql, sql_data):
	try:
		global c, con 
		c.execute(sql, sql_data)
		#con.commit()
	except (AttributeError, MySQLdb.OperationalError):
		c = connect()
		c.execute(sql, sql_data)
		#con.commit()


def update(query):
	try:
		global c, con
		c.execute(query)
		#con.commit()
	except (AttributeError, MySQLdb.OperationalError):
		c, con = connect()
		c.execute(query)
		#con.commit()
def delete(query):
	try:
		global c,con 
		#query = "DELETE FROM " + tabela + " WHERE " + where
		c.execute(query)
		con.commit()
	except (AttributeError, MySQLdb.OperationalError):
		c = connect()
		c.execute(query)
