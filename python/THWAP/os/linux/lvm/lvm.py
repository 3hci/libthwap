import sys, os, popen2
import types
import exceptions as ex

class thLvm2:
	def __init__(self):
		self.lvm = '/sbin/lvm'
	# Utility functions
	def _run(self, cmd):
		o = popen2.Popen3(cmd)
		buff = o.fromchild.readline()
		retv = []
		while buff != '':
			retv.append(buff.strip())
			buff = o.fromchild.readline()
		return retv

	def _flattenList(self, lst=[]):
		if type(lst) != types.ListType:
			raise ex.InvalidType, '_flattenList() Ivanlid argument type given.'
		else:
			if lst == []:
				raise ex.InvalidArgument, 'Invalid arguments passed to _flattenList()'
			else:
				retv = ''
				for i in lst:
					retv = retv+i+' '
				return retv
		return None

	# Physical volume functions
	def pvchange(self):
		return None

	def pvcreate(self, devs=[]):
		if type(devs) != types.ListType:
			raise ex.InvalidType, 'pvcreate() Invalid argument type given.'
		else:
			if devs == []:
				raise ex.InvalidArgument, 'Invalid arguments passed to pvcreate().'
			else:
				for a in devs:
					retv = self._run('echo "pvcreate %s" | %s' % (a, self.lvm))
					print retv[0].split('>')[1].strip()
		return None

	def pvdisplay(self):
		print self._run('echo "pvdisplay" | %s' % self.lvm)
		return None

	def pvmove(self):
		return None

	def pvremove(self, devs=[]):
		if type(devs) != types.ListType:
			raise ex.InvalidType, 'pvremove() Invalid argument type given.'
		else:
			if devs == []:
				raise ex.InvalidArgument, 'Invalid arguments given to pvremove().'
			else:
				for a in devs:
					retv = self._run('echo "pvremove %s" | %s' % (a, self.lvm))
					print retv[0].split('>')[1].strip()
		return None

	def pvresize(self):
		return None

	def pvs(self):
		return None

	def pvscan(self):
		print self._run('echo "pvscan" | %s' % self.lvm)
		return None

	# Volume group functions
	def vgcreate(self, group='', pvols=[]):
		if type(group) != types.StringType and type(pvols) != types.ListType:
			raise ex.InvalidType, 'vgcreate() Invalid argument type given.'
		else:
			if group == '' or pvols == []:
				raise ex.InvalidArgument, 'Invalid arguments passed to vgcreate().'
			else:
				args = self._flattenList(pvols)
				retv = self._run('echo "vgcreate %s %s" | %s' % (group, args, self.lvm))
				print retv[0].split('>')[1].strip()
			return None
		return None

	def vgextend(self):
		return None

	def vgresize(self):
		return None

	def vgremove(self, group=''):
		if type(group) != types.StringType:
			raise ex.InvalidType, 'vgremove() Invalid argument type given.'
		else:
			if group == '':
				raise ex.InvalidArgument, 'Invalid arguments passed to vgremove().'
			else:
				retv = self._run('echo "vgremove %s" | %s' % (group, self.lvm))
				print retv[0].split('>')[1].strip()
		return None

	def vgscan(self):
		print self._run('echo "vgscan" | %s' % self.lvm)
		return None

	def vgdisplay(self):
		print self._run('echo "vgdisplay" | %s' % self.lvm)
		return None

	# Logical volume functions
	def lvcreate(self, size='', name='', group=''):
		for i in (size, name, group):
			if type(i) != types.StringType:
				raise ex.InvalidType, 'lvcreate(): Invalid argument type given.'
			elif size == '' or name == '' or group == '':
				raise ex.InvalidArgument, 'lvcreate(): Invalid argument data given.'
			else:
				validM = size[(len(size) - 1)]
				for i in ['b','B','k','K','m','M','g','G','t','T']:
					if validM == i:
						break
				print self._run('echo "lvcreate -L%s -n%s %s" | %s' % (size, name, group))
		return None

	def lvextend(self):
		return None

	def lvresize(self):
		return None

	def lvremove(self, vol=[]):
		if type(vol) != types.ListType:
			raise ex.InvalidType, 'lvremove(): Invalid argument type given.'
		elif vol == []:
			raise ex.InvalidArgument, 'lvremove(): Invalid argument data given.'
		else:
			for i in vol:
				print self._run('echo "lvremove %s" | %s' % (i, self.lvm))
		return None

	def lvscan(self):
		print self._run('echo "lvscan" | %s' % self.lvm)
		return None

	def lvdisplay(self):
		print self._run('echo "lvdisplay" | %s' % self.lvm)
		return None

if __name__ == '__main__':
	o = LVM2()
	o.pvcreate(['/dev/sda1', '/dev/sda2', '/dev/sda3', '/dev/sda5', '/dev/sda6', '/dev/sda7'])
	o.vgcreate('group1', ['/dev/sda1', '/dev/sda2', '/dev/sda3'])
	o.vgcreate('group2', ['/dev/sda5', '/dev/sda6', '/dev/sda7'])

	o.vgremove('group1')
	o.vgremove('group2')
o.pvremove(['/dev/sda1', '/dev/sda2', '/dev/sda3', '/dev/sda5', '/dev/sda6', '/dev/sda7'])
