class ThSlurp
	def initialize
			@triggers = []
	end

	def registerTrigger(pattern, callback)
		if pattern == nil or callback == nil
			puts 'dumbass'
		else
			@triggers.push({'pattern' => pattern, 'callback' => callback})
		end
	end

	def process(file)
		if file == nil
			puts 'dumbass'
		else
			File.open(file).each { |line|
				@triggers.each { |trigger|
					if line =~ trigger['pattern']
						eval("#{trigger['callback']}('#{line}')")
					end 
				} 
			}
		end
	end

end

class ThConfig
	def initialize(file)
		self.slurp(file)
		@fp.close()
	end

	def slurp
		@conf = {}
		section = ''
		File.open(file).each { |line|
			if line.chomp != '' and line[0].chr != '#'
				if line =~ /^.*\{/
					@conf[line.split[0]] = {}
					section = line.split[0]
				elsif line =~ /^.*=.*/ and section != ''
					@conf[section][line.split('=')[0].chop] = line.split('=')[1].chop
				elsif line =~ /^.\}/
					section = ''
				end
			end 
		}
	end

	def lookup(section, key)
		@conf.each { |sectionKey|
			if sectionKey == section
				@conf[sectionKey].each { |hashKey|
					if hashKey == key
						return @conf[section][key]
					end
				} 
			end
		} 
		return false
	end

	def set(section, key, value)
		@conf.each { |sectionKey|
			if sectionKey == section
				@conf[section][key] = value
				return true
			end 
		}
		@conf[section] = {key => value}
		return true
	end
	
end
		

