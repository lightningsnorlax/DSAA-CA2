# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# HashTable Class
# -------------------------
class HashTable:

	# Constructor Function
	def __init__(self, initial_capacity=10, load_factor=0.7):
		self.__capacity = initial_capacity
		self.__size = 0
		self.__load_factor = load_factor
		self.__keys = [None] * self.__capacity
		self.__buckets = [None] * self.__capacity

	# A simple remainder method to convert key to index
	def __hash_function(self, key):
		return hash(key) % self.__capacity

	# Deal with collision resolution by means of
	# linear probing with a 'plus 1' rehash
	def __rehash_function(self, old_hash):
		return (old_hash + 1) % self.__capacity
	
	# Resize the hash table
	def resize(self, new_capacity):
		old_keys = self.__keys
		old_buckets = self.__buckets

		self.__capacity = new_capacity
		self.__keys = [None] * self.__capacity
		self.__buckets = [None] * self.__capacity
		self.__size = 0

		for key, value in zip(old_keys, old_buckets):
			if key is not None:
				self[key] = value
	
	# (key, value) insertion
	def __setitem__(self, key, value):
		index = self.hashFunction(key)
		startIndex = index
		while True:
			# If bucket is empty then just use it
			if self.__buckets[index] == None:
				self.__buckets[index] = value
				self.__keys[index] = key
				break
			else: # If not empty and the same key then just overwrite
				if self.__keys[index] == key:
					self.__buckets[index] = value
					break
				else: # Look for another available bucket
					index = self.rehashFunction(index)
					# We must stop if no more buckets
					if index == startIndex:
						break
	
	# Value retrieval from key
	def __setitem__(self, key, value):
		if (self.__size + 1) / self.__capacity > self.__load_factor:
			self.resize(self.__capacity * 2)

		index = self.__hash_function(key)
		start_index = index

		while True:
			# If bucket is empty then just use it
			if self.__keys[index] is None:
				self.__buckets[index] = value
				self.__keys[index] = key
				self.__size += 1
				break
			else:  # If not empty and the same key then just overwrite
				if self.__keys[index] == key:
					self.__buckets[index] = value
					break
				else:  # Look for another available bucket
					index = self.__rehash_function(index)
					# We must stop if no more buckets
					if index == start_index:
						break
					
	# Value retrieval from key
	def __getitem__(self, key):
		index = self.__hash_function(key)
		start_index = index

		while True:
			if self.__keys[index] == key: 
				return self.__buckets[index]
			else:
				index = self.__rehash_function(index)
				if index == start_index or self.__keys[index] is None:
					return None
				
	# Retrieve all keys
	def getAllKeys(self):
		return [key for key in self.__keys if key is not None]

	# Retrieve all items
	def getAllItems(self):
		return [(key, self.__buckets[i]) for i, key in enumerate(self.__keys) if key is not None]