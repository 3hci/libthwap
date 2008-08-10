import sys, types
from thUtils.stdlib import *
from threading import Thread

# Builtin Commands
class Commands:
	def __init__(self):
		return None

# Worker thread
class Worker(Thread):
	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		return False

class Scheduler:
	def __init__(self):
		return None

class Monitor:
	def __init__(self):
		cmd = Commands()
		self.commands = {}
		self.hosts = {}
		self.hostg = {'default': []}

	def _is_in_list(self, itm, lst):
		for item in lst:
			if itm == item: return True
		return False

	def _chk_str(self, itm):
		if type(itm) == types.StringType and itm != '': return True
		else: return False


	def register_command(self, cmd_name=None, cmd_cback=None):
		if cmd_name == None or cmd_cback == None:
			th_error('Invalid paramaters given to mstat.Monitor.register_command(cmd_name, cmd_cback)')
			return False
		else:
			if self._chk_str(cmd_name) == True:
				if type(cmd_cback) == types.FunctionType or type(cmd_cback) == types.MethodType:
					self.commands[cmd_name] = cmd_cback
					return True
				else:
					return False
  
	def register_host(self, host='', addr='', commands=[]):
		if self._chk_str(host) == True and self._chk_str(addr) == True:
			if self._is_in_list(host, self.hosts.keys()) == True:
				th_error('Trying to add duplicate host %s' % host)
				return False
			for i in commands:
				if self._is_in_list(i, self.commands.keys()) == False:
					th_error('Trying to add host %s with nonexisting command %s' % (host,i))
					return False
			self.hosts[host] = {'commands': commands, 'address': addr}
			return True
		else: return False

	def register_hostg(self, hostg='', members=[]):
		if self._chk_str(hostg) == True:
			if self._is_in_list(hostg, self.hostg.keys()) == True:
				th_error('Trying to add duplicate hostgroup %s' % hostg)
				return False
			for i in members:
				if self._is_in_list(i, self.hosts.keys()) == False:
					th_error('Trying to add nonexisting host %s to hostgroup %s' % (i, hostg))
					return False
			self.hostg[hostg] = members
			return True
		else: return False

	def hostg_member_add(self, hostg='', member=''):
		if self._chk_str(hostg) == True and self._chk_str(member) == True:
			if self._is_in_list(hostg, self.hostg.keys()) == False:
				th_error('Trying to add member to nonexisting hostgroup %s' % hostg)
				return False
			elif self._is_in_list(member, self.hosts.keys()) == False:
				th_error('Trying to add nonexisting host %s to hostgroup %s' % (member,hostg))
				return False
			if self._is_in_list(member, self.hostg[hostg]) == True:
				th_warn('Trying to add duplicate host %s to hostgroup %s' % (member,hostg))
				return False
			else:
				self.hostg[hostg].append(member)
				return True
		else: return False

	def check_host(self, host):
		if _is_in_list(host, self.hosts.keys()) == True:
			for cmd in self.hosts[host]['commands']:
				self.commands[host](self.hosts[host]['address'])

	def check_all(self):
		hgrps = self.hostg.keys()
		hgrps.sort()
		for grp in hgrps:
			hosts = self.hostg[grp]
			hosts.sort()
			for hst in hosts:
				print 'Checking '+hst
				for cmd in self.hosts[hst]['commands']:
					self.commands[cmd](self.hosts[hst]['address'])
