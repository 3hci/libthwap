#!/usr/bin/env python
import sys, os, time
sys.path.insert(0, '%s/../python/' % os.getenv('PWD'))

# python/THWAP/core/config.py unit tests
from THWAP.core import config
# thSlurp tests
thSlurpFlag = 0
def mprint(msg):
		global thSlurpFlag
		thSlurpFlag = 1

thSlurp = config.thSlurp()
fp = open('/tmp/thwap-py-unit-test-slurp', 'w+')
fp.write('this is a test\nbut this is not\n')
fp.close()
fp = open('/tmp/thwap-py-unit-test-slurp','r')
thSlurp.registerTrigger('^this.*', mprint)
thSlurp.process(fp)
if thSlurpFlag == 1:
	print 'thSlurp interface works as expected.' 
else:
	print 'thSlurp interface is not working as expected.'
os.unlink('/tmp/thwap-py-unit-test-slurp')

# thConfig tests
fp = open('/tmp/thwap-py-unit-test-config', 'w+')
fp.write('''testSection {
   testkey = testvalue
}''')
fp.close()
thConfig = config.thConfig('/tmp/thwap-py-unit-test-config')
if thConfig.conf != {} and thConfig.lookup('testSection', 'testkey') == 'testvalue':
	thConfig.set('testSection', 'testkey', 'anotherValue')
	if thConfig.lookup('testSection', 'testkey') == 'anotherValue':
		print 'thConfig interface works as expected.'
	else:
		print 'thConfig interface is not working as expected.'
else:
	print 'thConfig interface is not working as expected.'
os.unlink('/tmp/thwap-py-unit-test-config')
