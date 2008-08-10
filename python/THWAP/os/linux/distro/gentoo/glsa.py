#!/usr/bin/env python
#
# Copyright (c) 2007 Academic Superstore
# Copyright (c) 2007 Mike "Fuzzy" Partin <fuzzy@academicsuperstore.com>
#
# Program code
import sys, os, popen2
import mslurp

class GLSA:
	def __init__(self, user=None, host=None):
		self.host = host
		self.user = user
		self.garg = ''
		self.glsa = '/usr/bin/glsa-check'
		self.applied = {}
		self.unaffct = {}
		self.affectd = {}

	def add_unaffected(self, st=''):
		if st != '':
			tmp = st.strip().split()
			name = tmp[0]
			self.unaffct[name] = st.strip().split(st.strip().split()[1])[1].strip()
			self.print_status()
		else:
			return False

	def add_affected(self, st=''):
		if st != '':
			tmp = st.strip().split()
			name = tmp[0]
			self.affectd[name] = st.strip().split(st.strip().split()[1])[1].strip()
			self.print_status()
		else:
			return False

	def add_applied(self, st=''):
		if st != '':
			tmp = st.strip().split()
			name = tmp[0]
			self.applied[name] = st.strip().split(st.strip().split()[1])[1].strip()
			self.print_status()
		else:
			return False

	def print_status(self):
		sys.stdout.write('Applied:( %5d ) Unaffected:( %5d ) Affected:( %5d )\r' % (len(self.applied.keys()),len(self.unaffct.keys()),len(self.affectd.keys())))
		sys.stdout.flush()

	def check(self):
		if self.host == None:
			sys.stdout.write('Checking system security status ... \n')
		else:
			sys.stdout.write('Checking system security status on %s ... \n' % self.host)
		sys.stdout.write('Fetching current GLSA list...\r')
		sys.stdout.flush()
		self.slurp = mslurp.Proc()
		self.slurp.register_trigger({'t_pattern': '^[0-9]+.*\[U\]', 't_callback': self.add_unaffected})
		self.slurp.register_trigger({'t_pattern': '^[0-9]+.*\[A\]', 't_callback': self.add_applied})
		self.slurp.register_trigger({'t_pattern': '^[0-9]+.*\[N\]', 't_callback': self.add_affected})
		if self.host != None and self.user == None:
			obj = popen2.Popen4('ssh %s@%s "%s -ln"' % (os.getenv('USER'),self.host,self.glsa))
		elif self.host != None and self.user != None:
			obj = popen2.Popen4('ssh %s@%s "%s -nl"' % (self.user,self.host,self.glsa))
		else:
			obj = popen2.Popen4('%s -ln' % self.glsa)
		
		self.slurp.run(obj.fromchild)

		print ''
		for i in self.affectd.keys():
			sys.stdout.write('INFO: %s : %s\n' % (i, self.affectd[i]))

if __name__ == '__main__':
	o = GLSA()
	o.check()
