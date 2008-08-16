class thGlsa
	def initialize(user, host)
		if not user: @user = nil; end
		if not host: @host = nil; end
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
		puts "Applied:( #{@applied.len} ) Unaffected:( #{@unaffct.len} ) Affected:( #{@affectd.len}\r"
		return
	end

	def check
		if @host == nil
			puts "Checking system security status ... \n"
		else
			puts "Checking system security status on #{@host} ... \n"
		end
		puts "Fetching current GLSA list ... \r"
		# register thSlurp() instance
		# register trigger
		# register trigger
		# register trigger
		if @host == nil and @user == nil
			# define process pipe object
		elsif @host != nil and @user != nil
			# define process pipe object
		else
			# define last hope pipe object
		end
		# slurp the damn pipe object
		puts "\n"
		@affectd.each { |pkg|
			puts "INFO: #{pkg} : #{@affectd[pkg]}\n" }
	end
end
		return
	end


