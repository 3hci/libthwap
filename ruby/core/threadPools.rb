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
