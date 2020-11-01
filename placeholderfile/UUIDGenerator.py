import random
import string

class UUIDGenerator:

	def __init__(self, dtype='str-major', seed=None):
		self.dtype = dtype
		if seed is not None:
			self.seed = seed
		else:
			self.seed = random.randint(1, 200)
	def generate(self):
		if self.dtype == 'int-major':
			self.result = []
			length = 22
			data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '&', '-', '%', '#', '@']
			self.result = ''.join(random.choice(data) for i in range(length))

		elif self.dtype == 'str-major':
			length = 22
			letters = string.ascii_lowercase + string.ascii_uppercase + '-%$#@!&^*(){}[]><?/|'
			self.result = ''.join(random.choice(letters) for i in range(length))
		
		else:
			self.result = 'Unknown UUID data-type mentioned'

		return self.result