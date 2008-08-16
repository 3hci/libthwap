import re

class thSlurp:
	def __init__(self):
		self.triggers = []

	def registerTrigger(self, pattern='', callback=None:
		if pattern == '' or callback == None:
			# call error thingy
		else:
			try: self.triggers.append({'pattern': pattern, 'callback': callback)
			except: return False
		return True

	def process(self, fp=None):
		if fp != None:
			bf = fp.readline()
			while bf != '':
				for i in self.triggers:
					if re.match(i['pattern'],bf.strip()): 
						i['callback'](bf.strip())
				bf = fp.readline()

class thConfig:
	def __init__(self, file=''):
		self.file = file
		self.fp = open(file, 'r')
		self.slurp()
		self.fp.close()

	def slurp(self):
		self.conf = {}
		section = ''
		data = self.fp.readlines()
		for line in data:
			if line.strip() != '' and line[0] != '#':
				if re.match("^.*{", line) != None:
					self.conf[line.split()[0]] = {}
					section = line.split()[0].strip()
				elif re.match("^.*=.*", line) != None and section != '':
					self.conf[section][line.split('=')[0].strip()] = line.split('=')[1].strip()
				elif re.match("^.}", line) != None:
					section = ''
		return True

	def lookup(self, sect=None, key=None):
		if sect == None or key == None:
			return False
		else:
			try:
				return self.conf[sect][key]
			except:
				return False

	def set(self, sect=None, key=None, val=None):
		if sect == None or key == None or val == None:
			return False
		else:
			if not self.conf[sect]:
				self.conf[sect] = {}
			self.conf[sect][key] = val

