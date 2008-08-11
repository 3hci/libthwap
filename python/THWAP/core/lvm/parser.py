import sys, os, time
import types, re
from excpt import *

class thParser:
	def __init__(self):
		self.parseObj = []

	def stackCheck(self, key=''):
		if type(key) != types.StringType:
			raise InvalidType, 'parser.Parser.stackCheck(): Invalid argument type given.'
		elif key == '':
			raise InvalidArgument, 'parser.Parser.stackCheck(): Invalid argument data given.'
		else:
			for a in self.parseObj:
				if a['trigger'] == key:
					return True
		return False

	def regParseObj(self, trigg='', cback=None):
		if type(trigg) != types.StringType or type(cback) != types.FunctionType:
			raise InvalidType, 'parser.Parser.regParseObj(): Invalid argument type given.'
		elif trigg == '':
			raise InvalidArgument, 'parser.Parser.regParseObj(): Invalid argument data given.'
		else:
			if self.stackCheck(trigg) == False:
				self.parseObj.append({'trigger': trigg, 'callback': cback})
				return True
		return False

	def uregParseObj(self, trigg=''):
		if type(trigg) != types.StringType:
			raise InvalidType, 'parser.Parser.uregParseOj(): Invalid argument type given.'
		elif trigg == '':
			raise InvalidArgument, 'parser.Parser.uregParseOj(): Invalid argument data given.'
		else:
			cnt = 0
			for i in self.parseObj:
				if i['trigger'] == trigg:
					self.parseObj.pop(cnt)
					return True
				cnt += 1
		return False

	def defCallback(self, st=''):
		if type(st) != types.StringType:
			raise InvalidType, 'parser.Parser.defCallback(): Invalid argment type given.'
		elif st == '':
			raise InvalidArgument, 'parser.Parser.defCallback(): Invalid argument data given.'
		else:
			print st
			return True
		return False

	# The parser class is a generic parser that will go through a given
	# list, where each item in the list is a string, for each of these
	# strings, the parser will go through it's registered list of triggers
	# and fire off their corresponding callacks if they are matched with
	# the string they matched against as the single argument.
	def parse(self, st=''):
		if type(st) != types.StringType:
			raise InvalidType, 'parser.Parser.parse(): Invalid argument type given.'
		elif st == '':
			raise InvalidArgument, 'parser.Parser.parse(): Invalid argument data given.'
		else:
			for a in self.parseObj:
				if re.match(a['trigger'], st) != None:
					a['callback'](st)
					return True
		return False

def test(st):
	print st

if __name__ == '__main__':
	o = Parser()
	o.regParseObj('^H.*oy.', test)
	o.parse('This is a test')
	o.parse('He was a jerk')
	o.parse('Here is the toy')
	o.parse('Here is the toy.')
