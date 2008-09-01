module THWAP
	module Core
		class ThSlurp
			def initialize
				@flagged = nil
				@triggers = []
			end
	
			def registerTrigger(pattern, callback)
				if pattern == nil or callback == nil
					puts 'dumbass'
				else
					@triggers.push((pattern, callback))
				end
			end

			def unregisterTrigger(pattern, callback)
				if pattern == nil or callback == nil
					puts 'dumbass'
				else
					index = @triggers.index((pattern, callback))
					if index != nil
						@triggers.pop(index)
					end
				end
			end

			def setFlag(index)
				self.registerTrigger(/^.*/, @triggers[index][1])
				if @flagged == nil
					@flagged = index
				else
					return false
				end
			end

			def unsetFlag(index)
				if index == nil
					return false
				else
					if @flagged == nil
						return false
					else
						@flagged = nil
						self.unregisterTrigger(/^.*/, @triggers[index][1])
					end
				end
			end

			def process(file)
				if file == nil
					puts 'dumbass'
				else
					file.each { |line|
						@triggers.each { |trigger|
							if line =~ /trigger['pattern']/
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
	end
end

