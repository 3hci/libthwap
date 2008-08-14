class thSlurp
	def initialize
			@triggers = []
	end

	def regCallBack(pattern, callback)
		if pattern == nil or callback == nil
			puts 'dumbass'
		else
			@triggers.push({'pattern' => pattern, 'callback' => callback})
		end
	end

	def run(file)
		if file == nil
			puts 'dumbass'
		else
			File.open(file).each { |line|
				@triggers.each { |trigger|
					if line =~ trigger.pattern
						puts "#{line} - #{trigger.pattern.to_s}"
					end } }
		end
	end

end

class thConfig
	def initialize(file)
		self.slurp(file)
		@fp.close()
	end

	def slurp
		@conf = {}
		section = ''
		File.open(file).each { |line|
			if line.chomp != '' and line[0].chr != '#'
				if line =~ /^.*{/
					@conf[line.split[0]] = {}
					section = line.split[0]
				elsif line =~ /^.*=.*/ and section != ''
					@conf[section][line.split('=')[0].chop] = line.split('=')[1].chop
				elsif line =~ /^.}/
					section = ''
				end
		end }
	end

	def lookup(section, key)
		@conf.each { |sect_key|
			if sect_key == section
				@conf[sect_key].each { |hash_key|
					if hash_key == key
						return @conf[section][key]
					end
			} end
		} return false
	end

	def set(section, key, value)
		@conf.each { |sect_key|
			if sect_key == section
				@conf[section][key] = value
				return true
			end }
		@conf[section] = {key => value}
		return true
	end
	
end
		

