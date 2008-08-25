#!/usr/bin/env python
import sys
import os
import time
import random
import unittest

# Setup our library paths depending on whether or not we are being run by
# hand or from the Makefile.
if os.getenv('PWD').find('test') == -1:
	sys.path.insert(0, "%s/python/" % os.getenv('PWD'))
else:
	sys.path.insert(0, '%s/../python/' % os.getenv('PWD'))

# imports to test
from THWAP.core import config
from THWAP.os.linux.gentoo import glsa

# libTHWAP unit tests
class unitTest(unittest.TestCase):
		def setUp(self):
			# THWAP.core.config.thSlurp()
			self.thSlurpFlag = 0
			self.thSlurp = config.thSlurp()

		def thSlurpCallback(self, msg):
			self.thSlurpFlag = 1

		def testslurp(self):
			fp = open('/tmp/thwap', 'w+')
			fp.write('this is a test\nbut this is not\n')
			fp.close()
			fp = open('/tmp/thwap', 'r')
			self.thSlurp.registerTrigger('^this.*', self.thSlurpCallback)
			self.thSlurp.process(fp)
			os.unlink('/tmp/thwap')
			self.assertEqual(self.thSlurpFlag, 1)

		def testconfig(self):
			fp = open('/tmp/thwap', 'w+')
			fp.write('''# Comment
testSection {
	testkey = testvalue
}\n''')
			fp.close()
			self.thConfig = config.thConfig('/tmp/thwap')
			if self.thConfig.conf != {}:
				if self.thConfig.lookup('testSection', 'testkey') == 'testvalue':
					self.thConfig.set('testSection', 'testkey', 'anotherValue')
			self.assertEqual(self.thConfig.lookup('testSection', 'testkey'), 'anotherValue')

if __name__ == '__main__':
	unittest.main()
