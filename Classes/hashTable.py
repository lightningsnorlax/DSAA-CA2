# -------------------------
# HashTable Class
# -------------------------
class HashTable:

	# Constructor Function
	def __init__(self, size):
		self.size = size
		self.keys = [None] * self.size
		self.buckets = [None] * self.size

	# A simple remainder method to convert key to index
	def hashFunction(self, key):
		#return key % self.size
		return hash(key) % self.size

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
	def rehashFunction(self, oldHash):
		return (oldHash + 1) % self.size
	
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
	def __getitem__(self, key):
		index = self.hashFunction(key)
		startIndex = index
		while True:
			if self.keys [index] == key: # Will be mostly the case unless value had been previously rehashed at insertion time
				return self.buckets[index]
			else: # Value for the key is somewhere else (due to imperfect hash function)
				index = self.rehashFunction(index)
				if index == startIndex:
					return None
				
	# Retrieve all keys
	def getAllKeys(self):
		return [key for key in self.keys if key is not None]
	
	# Retrieve all items
	def getAllItems(self):
		return [(key, self.buckets[i]) for i, key in enumerate(self.keys) if key is not None]

	
# Issues to relook at
# relook at hash function, getAllKeys, getAllItems