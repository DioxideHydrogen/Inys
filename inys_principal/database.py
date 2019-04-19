import MySQLdb

host = 'localhost'
user = 'alexa_login'
password = '19862010'
banco = 'alexa_db'
porta = 3306

con = MySQLdb.connect(host,user,password,banco,porta)
c = con.cursor(MySQLdb.cursors.DictCursor)


def connect():
	host = 'localhost'
	user = 'alexa_login'
	password = '19862010'
	banco = 'alexa_db'
	porta = 3306

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
