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
		@unaffct[st.chomp.chop.split[0]] = st.chomp.chop.split(st.chomp.chop.split[1])[1].chomp
	end

	def addAffected(st)
		@affectd[st.chomp.chop.split[0]] = st.chomp.chop.split(st.chomp.chop.split[1])[1].chomp
	end

	def addApplied(st)
		@applied[st.chomp.chop.split[0]] = st.chomp.chop.split(st.chomp.chop.split[1])[1].chomp
	end

	def printStatus
		return
	end

	def check
		return
	end


