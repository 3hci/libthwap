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
					end
				}
			}
		end
	end

end

class thConfig
	def initialize(file)
		@fp = File.open(file)
		self.slurp()
		@fp.close()
	end

	def slurp
		@conf = {}
	end
		

