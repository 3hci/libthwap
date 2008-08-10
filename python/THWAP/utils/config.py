import re

class Config:
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
					section == ''
		return True

	def dump(self):
		try:
			self.fp = open(self.file, 'w+')
			for a in self.conf.keys():
				self.fp.write(a+' {\n')
				for b in self.conf[a].keys():
					self.fp.write('\t'+b+' = '+self.conf[a][b]+'\n')
				self.fp.write('}\n')
				self.fp.flush()
			self.fp.close()
			return True
		except:
			return False

	def lookup(self, sect=None, key=None):
		if sect == None or key == None:
			return False
		else:
			try:
				return self.conf[sect][key]
			except:
				return False

	def set(self, sect=None, key=None):
		if sect == None or key == None or val == None:
			return False
		else:
			if not self.conf[sect]:
				self.conf[sect] = {}
			self.conf[sect][key] = val

