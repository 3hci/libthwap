import sys
import os, MySQLdb

class thDBase:
	def __init__(self, hostname='', username='', password='', database=''):
		if hostname == '': raise ex.InvalidHostname, 'ERROR: The hostname provided to db.DBase() was invalid.'
		if username == '': username = os.getenv('USER')
		if password == '' and database == '':
			self.db = MySQLdb.connect(host=hostname, user=username)
		elif password == '' and database != '':
			self.db = MySQLdb.connect(host=hostname, user=username, db=database)
		elif password != '' and database == '':
			self.db = MySQLdb.connect(host=hostname, user=username, passwd=password)
		elif password != '' and database != '':
			self.db = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
		self.cr = self.db.cursor()
		self.connInfo = {'server': hostname, 'user': username, 'passwd': password, 'db': database}

	def databases(self):
		dbases = []
		self.cr.execute('SHOW DATABASES;')
		for row in self.cr:
			for i in row:
				dbases.append(i)
		return dbases

	def tables(self, dbase):
		tables = []
		self.cr.execute('USE %s;' % dbase)
		self.cr.execute('SHOW TABLES;')
		for row in self.cr:
			for i in row:
				tables.append(i)
		return tables

class thDB:
	def __init__(self, hostname='', username='', password=''):
		if hostname == '': hostname = localhost
		if username == '': username = os.getenv('USER')
