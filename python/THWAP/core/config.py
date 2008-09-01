import re

class thSlurp:
	def __init__(self):
		self.triggers = []
		self.flagged = None

	def registerTrigger(self, patt='', cback=''):
		if patt == '' or cback == '':
			return False
		else:
			try: self.triggers.append((patt, cback))
			except: return False
		return True
	
	def unregisterTrigger(self, patt='', cback=''):
		if patt == '' or cback == '':
			return False
		else:
			for i in range(0, len(self.triggers)):
				if self.triggers[i][0] == patt:
					self.triggers.pop(i)
					return True

	def setFlag(self, index=None):
		if index == None:
			return False
		else:
			self.registerTrigger('^.*', self.triggers[index][1])
			if self.flagged == None: self.flagged = index
			else: return False
			return True

	def unsetFlag(self, index=None):
		if index == None:
			return False
		else:
			if self.flagged == None: 
				return False
			else:
				self.flagged = None
				self.unregisterTrigger('^.*', self.triggers[index][1])
				return True

	def getIndex(self, pattern=None):
		if pattern != None:
			for i in range(0,(len(self.triggers)-1)):
				if self.triggers[i][0] == pattern:
					return i
			return None
		else: return None

	def process(self, fp=None):
		if fp != None:
			bf = fp.readline()
			while bf != '':
				for i in self.triggers:
					if re.match(i[0],bf.strip()): 
						i[1](bf.strip(), self.getIndex(i[0]))
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

