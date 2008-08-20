# Class: ThSpawnThread
# Author: Mike "Fuzzy" Partin
# Notes: Spawn a quick worker thread.
# TODO:  Still don't know how to pass the arguments I want,
class ThSpawnThread
	def initialize(func, *args)
		t = Thread.new{func4()}
		t.join
	end
end

class ThThreadObj
	def initialize
		@function = nil
		@args = ()
	end

	def regWorkLoad(func, args)
		if @function == nil
			@function = func
		end
		if @args == ()
			@args.push(args)
		end
	end

	def run
		ThSpawnThread.new(@function, @args)
	end
end

# Class: ThThreadPool
# Author: Mike "Fuzzy" Partin
# Notes: Not done yet, but will be a pool of generic threads
class ThThreadPool
	def initialize(threads)
		@threadPool = ()
	  if threads.is_a?(Integer)
			threads.downto(1) { |iter|
				@threadPool.push(ThThreadObj.new)
			}
		end
	end
