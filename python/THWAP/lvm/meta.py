import os, sys, popen2, re
import core

class Volume:
	def __init__(self):
		self.attribs = {}
	
	def is_attr(self, attr=None):
		if attr != None:
			for i in self.attribs.keys():
				if i == attr:
					return True
		return False

	def set_attr(self, attr=None, val=None):
		if attr != None and val != None:
			self.attribs[attr] = val

	def get_attr(self, attr=None):
		if attr != None and self.is_attr(attr) == True:
			return self.attribs[attr]
		else:
			return False


class metaLVM(LVM_Base):
	def __init__(self):
		self.lvm_map()

	def lvm_map(self):
		self.mapper = []
		o = popen2.Popen3('/sbin/lvscan')
		buff = o.fromchild.readline()
		while buff != '':
			tmp = re.sub('\'', '', buff)
			tmps = tmp.strip().split()
			self.mapper.append([tmps[1], tmps[2][1:], tmps[3][:2]]) 
			buff = o.fromchild.readline()


if __name__ == '__main__':
	o = LVM2()
	print dir(o)
	print o.mapper
