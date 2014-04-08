class Stack:

	def __init__(self, start):
		self.contents = {}
		self.contents[start] = "-----"

	def get_contents(self):
		return self.contents
		
	def store_word(self, location, item):
		self.contents[location] = item
		
	def load_word(self, location):
		if not location in self.contents:
			return 0
		else:
			return self.contents[location]
