# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# HashTable Class
# -------------------------
class HashTable:

	# Constructor Function
	def __init__(self, initial_capacity=10, load_factor=0.7):
		self.capacity = initial_capacity
		self.size = 0
		self.load_factor = load_factor
		self.keys = [None] * self.capacity
		self.buckets = [None] * self.capacity

	# A simple remainder method to convert key to index
	def hash_function(self, key):
		return hash(key) % self.capacity

		# Source Credits: https://cp-algorithms.com/string/string-hashing.html
		# p = 31
		# m = 10**9 + 9
		# hash_value = 0
		# p_pow = 1

		# for c in key:
		# 	hash_value = (hash_value + (ord(c) - ord('a') + 1) * p_pow) % m
		# 	p_pow = (p_pow * p) % m

		# hash_value = hash(key)
		# print(hash_value)

		#return hash_value

	# Deal with collision resolution by means of
	# linear probing with a 'plus 1' rehash
	def rehash_function(self, old_hash):
		return (old_hash + 1) % self.capacity
	
	# Resize the hash table
	def resize(self, new_capacity):
		old_keys = self.keys
		old_buckets = self.buckets

		self.capacity = new_capacity
		self.keys = [None] * self.capacity
		self.buckets = [None] * self.capacity
		self.size = 0

		for key, value in zip(old_keys, old_buckets):
			if key is not None:
				self[key] = value

	
	# (key, value) insertion
	def __setitem__(self, key, value):
		index = self.hashFunction(key)
		startIndex = index
		while True:
			# If bucket is empty then just use it
			if self.buckets[index] == None:
				self.buckets[index] = value
				self.keys[index] = key
				break
			else: # If not empty and the same key then just overwrite
				if self.keys[index] == key:
					self.buckets[index] = value
					break
				else: # Look for another available bucket
					index = self.rehashFunction(index)
					# We must stop if no more buckets
					if index == startIndex:
						break
	
	# Value retrieval from key
	def __setitem__(self, key, value):
		if (self.size + 1) / self.capacity > self.load_factor:
			self.resize(self.capacity * 2)

		index = self.hash_function(key)
		start_index = index

		while True:
			# If bucket is empty then just use it
			if self.keys[index] is None:
				self.buckets[index] = value
				self.keys[index] = key
				self.size += 1
				break
			else:  # If not empty and the same key then just overwrite
				if self.keys[index] == key:
					self.buckets[index] = value
					break
				else:  # Look for another available bucket
					index = self.rehash_function(index)
					# We must stop if no more buckets
					if index == start_index:
						break
					
	# Value retrieval from key
	def __getitem__(self, key):
		index = self.hash_function(key)
		start_index = index

		while True:
			if self.keys[index] == key: 
				return self.buckets[index]
			else:
				index = self.rehash_function(index)
				if index == start_index or self.keys[index] is None:
					return None
				
	# Retrieve all keys
	def getAllKeys(self):
		return [key for key in self.keys if key is not None]

	# Retrieve all items
	def getAllItems(self):
		return [(key, self.buckets[i]) for i, key in enumerate(self.keys) if key is not None]