class Throbber:
	def __init__(self):
		self.throb = ['.','o','O','0','O','o','.']
		self.pos = 0
		self.mps = 6

	def next(self):
		if self.pos < self.mps:
			self.pos += 1
		elif self.pos == self.mps:
			self.pos = 0
		return self.throb[self.pos]

class Spinner(Throbber):
	def __init__(self):
		Throbber.__init__(self)
		self.throb = ['-','\\','|','/','-']
		self.mps = 4

class Progress:
	def __init__(self):
		self.prc = 0
		self.prog = '[          ]'

	def update(self, prc):
		self.prc = prc
		if prc >= 10 and prc < 20: self.prog = '[#         ]'
		elif prc >= 20 and prc < 30: self.prog = '[##        ]'
		elif prc >= 30 and prc < 40: self.prog = '[###       ]'
		elif prc >= 40 and prc < 50: self.prog = '[####      ]'
		elif prc >= 50 and prc < 60: self.prog = '[#####     ]'
		elif prc >= 60 and prc < 70: self.prog = '[######    ]'
		elif prc >= 70 and prc < 80: self.prog = '[#######   ]'
		elif prc >= 80 and prc < 90: self.prog = '[########  ]'
		elif prc >= 90 and prc < 100: self.prog = '[######### ]'
		elif prc >= 100: self.prog = '[##########]'
		return self.prog

