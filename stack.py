# USES TABS FOR INDENTATION
class Stack:

	def __init__(self):
		self.contents = dict()
		self.contents[0] = 0

	def get_contents(self):
		return self.contents
		
	def store_word(self, location, item):
		self.contents[location] = item
		
	def load_word(self, location):
		return self.contents[location]
