# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
from Classes.binaryTree import BinaryTree

# -------------------------
# BST Class
# -------------------------
class BST(BinaryTree): 

	# Constructor Function
	def __init__(self, key, leftTree = None, rightTree = None): 
		super().__init__(key,leftTree,rightTree)
	
	# Add Function: add new nodes as leafs
	def add(self, key): 
		curNode = self 
		while True:
			if key < curNode.key: 
				if curNode.leftTree == None: 
					curNode.leftTree = BST(key) 
					break 
				else:
					curNode= curNode.leftTree
			elif key > curNode.key: 
				if curNode.rightTree == None: 
					curNode.rightTree = BST(key) 
					break 
				else:
					curNode= curNode.rightTree
	
	# Search Function: search for items stored in tree
	def __contains__(self, key):
		curNode = self # Set currentNode to root key
		while True:
			if key == curNode.key: 
				return True
			elif key < curNode.key: # If less than parent key, go left
				if curNode.leftTree == None: # Check if left tree is empty
					return False 
				else:
					curNode = curNode.leftTree # Set currentNode to left tree key
			elif key > curNode.key: # If more than parent key, go right
				if curNode.rightTree == None: # Check if right tree is empty
					return False
				else:
					curNode= curNode.rightTree # Set currentNode to right tree key