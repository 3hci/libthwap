import os, sys
import syslog

class thSysLogger:
	def __init__(self, ident='libTHWAP: ')
		self.ident = ident
		syslog.openlog(ident)

# LOG_EMERG, LOG_ALERT, LOG_CRIT, LOG_ERR, LOG_WARNING, LOG_NOTICE, LOG_INFO, LOG_DEBUG. 
	def logEmerg(self, msg): syslog.syslog(syslog.LOG_EMERG, msg)
	def logAlert(self, msg): syslog.syslog(syslog.LOG_ALERT, msg)
	def logCrit(self, msg): syslog.syslog(syslog.LOG_CRIT, msg)
	def logErr(self, msg): syslog.syslog(syslog.LOG_ERR, msg)
	def logWarn(self, msg): syslog.syslog(syslog.LOG_WARNING, msg)
	def logNotice(self, msg): syslog.syslog(syslog.LOG_NOTICE, msg)
	def logInfo(self, msg): syslog.syslog(syslog.LOG_INFO, msg)
	def logDebug(self, msg): syslog.syslog(syslog.LOG_DEBUG, msg)

	def cleanup(self):
		syslog.closelog()
