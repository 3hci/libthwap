class thGlsa
	def initialize(user, host)
		if not user: @user = `whoami`; end
		if not host: @host = 'localhost'; end
		@garg = ''
		@glsa = `which glsa-check`
		if not @glsa: puts 'Are you sure your on Gentoo?'; exit; end
		@applied = {}
		@unaffct = {}
		@affectd = {}
	end

	def addUnaffected(st)
		tmp = st.chomp.chop.split
		name = tmp[0]
		@unaffct[name] = st.chomp.chop.split(st.chomp.chop.split[1])[1].chomp
	end

	def addAffected(st)
		return
	end

	def addApplied(st)
		return
	end

	def printStatus
		return
	end

	def check
		return
	end


