# HashMap implementation in Python

class HashMap(object):
	"""
	This class represents implementation of a hash map 
	where the key should be a string with with minimum 
	length of 2 characters.
	
	Attributes:
		map : List to store key_value against the key_hash.
	"""
	def __init__(self):
		"""
		The constructor for class HashMap.
		
		Parameters :
			map : List to store key_value against the key_hash.
		"""
		self.map = [None]*10000

	def _get_hash(self, key):
		"""
		The function to get hash value for the input key.
		
		Parameters :
			key : Key for which we need a hash value.
				  Key should have minimum length of 2 characters.

		Returns :
			key_hash : Hash value for the input key.
		"""
		return ord(key[0])*100 + ord(key[1])
		
	def add(self, key, value):
		"""
		The function to add new key value pair in the hashmap
		or update a value for an existing key in the map.
		
		Parameters :
			key : Input key to retreive data from hashmap.
			value : Value to be stored corresponding to the key in the hashmap.
		"""
		key_hash = self._get_hash(key)
		key_value = (key, value)
		
		if not self.map[key_hash]:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
	
	def get(self, key):
		"""
		The function retreives a value from the hashmap based upon the input key.
		
		Parameters :
			key : Input key to retreive data from hashmap.
		
		Returns : 
			value : Value stored in the hashmap corresponding to the input key.
		"""
		key_hash = self._get_hash(key)
		
		if self.map[key_hash]:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
		
	def delete(self, key):
		"""
		The function to delete a key_value pair from the hashmap.
		
		Parameters :
			key : Input key for which data is to be deleted.
		"""
		key_hash = self._get_hash(key)
		
		if not self.map[key_hash]:
			return False
		else:
			for i in range(len(self.map[key_hash])):
				if self.map[key_hash][i][0] == key:
					self.map[key_hash].pop(i)
					return True
	
	def print(self):
		"""
		The function to print contents of hashmap.
		"""
		for item in self.map:
			if item:
				print(str(item))
	