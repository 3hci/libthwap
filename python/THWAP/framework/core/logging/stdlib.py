import sys, types
sys.path.insert(0, '::PREFIX::/lib')
from thUtils import logger

ASUTILS_LOG = logger.Log('thUtils')

def th_error(st):
	if type(st) == types.StringType and st != '':
		sys.stderr.write('ERROR: %s\n' % st.strip())
		ASUTILS_LOG.error('ERROR: %s' % st.strip())
	else:
		return False

def th_warn(st):
	if type(st) == types.StringType and st != '':
		sys.stderr.write('WARNING: %s\n' % st.strip())
		ASUTILS_LOG.warning('WARNING: %s' % st.strip())
	else:
		return False

def th_fatal(st):
	if type(st) == types.StringType and st != '':
		sys.stderr.write('FATAL ERROR: %s\n' % st.strip())
		ASUTILS_LOG.error('FATAL ERROR: %s' % st.strip())
		sys.exit(-1)
	else:
		return False
