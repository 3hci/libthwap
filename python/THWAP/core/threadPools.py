from threading import Thread
import thread, time

# Class: thSpawnThread:
# Authro: Mike "Fuzzy" Partin
# Notes: Spawn a quick thread to do a quick job
class thSpawnThread:
	def __init__(self, func, *args):
		thread.start_new_thread(func, (args))
		return None

# Class: thThreadObj
# Author: Mike "Fuzzy" Partin
# Notes: Generic thread object
class thThreadObj(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.function = None
		self.args = None

	def regWorkLoad(self, function, *args):
		if self.function == None: self.function = function
		if self.args == None: self.args = args

	def run(self):
		if self.args != None:
			self.function(self.args)
		else:
			self.function()

# Class: thThreadPool
# Author: Mike "Fuzzy" Partin
# Notes: Just a pool of generic thread objects
#        Also of note, is this class is not finished
class thThreadPool:
		def __init__(self, threads=5):
			self.pool = []
			for i in range(threads):
					self.pool.append(thThreadObj())
			return None
			obj = thThreadObj()
			obj.regWorkLoad(refillPool, threads)
			obj.run()
			return None

		def refillPool(self, threads):
			while True:
				while len(self.pool) < threads:
					self.pool.append(thThreadObj())
				time.sleep(5)
