#!/usr/bin/env python
import os, sys, re, types
import exceptions as ex

class Config:
	def __init__(self, file=''):
		if type(file) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.__init__(): Invalid argument type given.'
		elif file == '' or os.path.isfile(file) == False:
			raise ex.InvalidArgument, 'atlas.config.Config.__init__(): Invalid argument data given.'
		else:
			self.CONFIG_FILE = file
			if not os.path.isfile(self.CONFIG_FILE):
				print 'ERROR: Config file %s not found.' % self.CONFIG_FILE
			else:
				self.config = {}
				self.slurpConfig()
	
	def slurpConfig(self):
		cat = ''
		item = ''
		fp = open(self.CONFIG_FILE, 'r')
		buff = fp.readline()
		while buff != '':
			if buff.strip()[0] != '#':
				if re.match('^\[.*\]', buff.strip()) != None:
					cat = buff.strip().split('[')[1].split(']')[0]
					self.config[cat] = {}
				elif re.match('.*{', buff.strip()) != None:
					item = buff.strip().split()[0]
					self.config[cat][item] = {}
				elif buff.strip() == '}':
					item = ''
				else:
					(key, val) = buff.strip().split('=')
					self.config[cat][item][key.strip()] = val.strip()
			buff = fp.readline()

	def haveCategory(self, cat=''):
		if type(cat) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.haveCategory(): Invalid argument type given.'
		elif cat == '':
			raise ex.InvalidArgument, 'atlas.config.Config.haveCategory(): Invalid argument data given.'
		else:
			for a in self.config.keys():
				if a == cat:
					return True
		return False

	def getCategory(self, cat=''):
		if type(cat) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.getCategory(): Invalid argument type given.'
		elif cat == '':
			raise ex.InvalidArgument, 'atlas.config.Config.getCategory(): Invalid argument data given.'
		else:
			if self.haveCategory(cat) == True:
				return self.config[cat]
		return False

	def haveGroup(self, cat='', grp=''):
		if type(cat) != types.StringType or type(grp) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.haveGroup(): Invalid argument type given.'
		elif grp == '' or cat == '':
			raise ex.InvalidArgument, 'atlas.config.Config.haveGroup(): Invalid argument data given.'
		else:
			if self.haveCategory(cat) == False:
				raise ex.InvalidCategory, 'atlas.config.Config.haveGroup(): Category (%s) does not exist.' % cat
			else:
				for a in self.config[cat]:
					if a == grp:
						return True
		return False

	def getGroup(self, cat='', grp=''):
		if type(cat) != types.StringType or type(grp) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.getGroup(): Invalid argument type given.'
		elif cat == '' or grp == '':
			raise ex.InvalidArgument, 'atlas.config.Config.getGroup(): Invalid argument data given.'
		else:
			if self.haveGroup(cat, grp) == True:
				return self.config[cat][grp]
		return False

	def haveItem(self, cat='', grp='', itm=''):
		if type(cat) != types.StringType or type(grp) != types.StringType or type(itm) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.haveItem(): Invalid argument type given.'
		elif cat == '' or grp == '' or itm == '':
			raise ex.InvalidArgument, 'atlas.config.Config.haveItem(): Invalid argument data given.'
		else:
			if self.haveGroup(cat, grp) == True:
				for a in self.config[cat][grp].keys():
						if a == itm:
							return True
		return False

	def getItem(self, cat='', grp='', itm=''):
		if type(cat) != types.StringType or type(grp) != types.StringType or type(itm) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.getItem(): Invalid argument type given.'
		elif cat == '' or grp == '' or itm == '':
			raise ex.InvalidArgument, 'atlas.config.Config.getItem(): Invalid argument data given.'
		else:
			if self.haveItem(cat, grp, itm) == True:
				return self.config[cat][grp][itm]
		return False

	def haveKey(self, cat='', grp='', itm='', key=''):
		if type(cat) != types.StringType or type(grp) != types.StringType or type(itm) != types.StringType or type(key) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.haveKey(): Invalid argument type given.'
		elif cat == '' or grp == '' or itm == '' or key == '':
			raise ex.InvalidArgument, 'atlas.config.Config.haveKey(): Invalid argument data given.'
		else:
			if self.haveItem(cat, grp, itm) == True:
				for a in self.config[cat][grp][itm].keys():
					if a == key:
						return True
		return False

	def getKey(self, cat='', grp='', itm='', key=''):
		if type(cat) != types.StringType or type(grp) != types.StringType or type(itm) != types.StringType or type(key) != types.StringType:
			raise ex.InvalidType, 'atlas.config.Config.getKey(): Invalid argument type given.'
		elif cat == '' or grp == '' or itm == '' or key == '':
			raise ex.InvalidArgument, 'atlas.config.Config.getKey(): Invalid argument data given.'
		else:
			if self.haveItem(cat, grp, itm) == True:
				return self.config[cat][grp][itm][key]
		return False

	def prettyPrint(self):
		print "ATLAS LVM Management Tool"
		print "Categories:"
		for a in self.config.keys():
			print '\t'+a
		print ''
		for b in self.config.keys():
			print 'Volume Group: '+b
			for c in self.config[b].keys():
				print '\t'+c
				for d in self.config[b][c].keys():
					print '\t\t'+d+' = '+self.config[b][c][d]


if __name__ == '__main__':
	o = Config()
	o.prettyPrint()
