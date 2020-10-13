import random
import string

def generateName(suffix = None, prefix = None, seed=None):
	length = 10
	if seed is not None:
		random.seed = seed

	letters = string.ascii_lowercase
	filename = ''.join(random.choice(letters) for i in range(length))
	
	if suffix is None and prefix is None:
		return filename
	elif suffix is not None and prefix is None:
		return filename + suffix
	elif suffix is None and prefix is not None:
		return prefix + filename
	else:
		return prefix + filename + suffix