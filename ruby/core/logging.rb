require 'syslog'

class thSysLogger
	def initialize(ident)
		if ident == '': ident = $0; end
		Syslog.open(ident)
	end

	def logCrit(msg): Syslog.crit(msg); end
	def logEmerg(msg): Syslog.emerg(msg); end
	def logAlert(msg): Syslog.alert(msg); end
	def logErr(msg): Syslog.err(msg); end
	def logWarn(msg): Syslog.warn(msg); end
	def logNotice(msg): Syslog.notice(msg); end
	def logInfo(msg): Syslog.info(msg); end
	def logDebug(msg): Syslog.debug(msg); end

	def cleanup
		Syslog.close
	end
end
