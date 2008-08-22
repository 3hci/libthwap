#!/usr/bin/env python
import sys, os, time
sys.path.insert(0, '%s/../python/' % os.getenv('PWD'))

# python/THWAP/core/config.py unit tests
from THWAP.core import config
# thSlurp tests
def mprint(msg):
		print msg

thSlurp = config.thSlurp()
fp = open('/tmp/thwap-py-unit-test-slurp', 'w+')
fp.write('this is a test\nbut this is not\n')
fp.close()
fp = open('/tmp/thwap-py-unit-test-slurp','r')
thSlurp.registerTrigger('^this.*', mprint)
thSlurp.registerTrigger('^but.*', mprint)
thSlurp.process(fp)
os.unlink('/tmp/thwap-py-unit-test-slurp')

# thConfig tests
fp = open('/tmp/thwap-py-unit-test-config', 'w+')
fp.write('''testSection {
   testkey = testvalue
}''')
fp.close()
thConfig = config.thConfig('/tmp/thwap-py-unit-test-config')
print thConfig.conf
print thConfig.lookup('testSection', 'testkey')
thConfig.set('testSection', 'testkey', 'anotherValue')
print thConfig.conf
print thConfig.lookup('testSection', 'testkey')
os.unlink('/tmp/thwap-py-unit-test-config')
