import logging

class thLog:
	def __init__(self, name=''):
		logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s',filename='/tmp/myapp.log',filemode='w')

	def error(self, msg=''):
		if msg != '': logging.debug(msg.strip())
	
	def debug(self, msg=''):
		if msg != '': logging.debug(msg.strip())

	def info(self, msg=''):
		if msg != '': logging.info(msg.strip())

	def warning(self, msg=''):
		if msg != '': logging.warning(msg.strip())

