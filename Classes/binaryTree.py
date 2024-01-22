# -------------------------
# BinaryTree Class
# -------------------------
class BinaryTree:

    # Constructor Function
    def __init__(self, key, leftTree = None, rightTree = None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree
	
	# Access functions
    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftTree

    def getRightTree(self):
        return self.rightTree

    def insertLeft(self, key):
        if self.leftTree == None:
            self.leftTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.leftTree , t.leftTree = t, self.leftTree
	
    def insertRight(self, key):
        if self.rightTree == None:
            self.rightTree = BinaryTree(key)
        else:
            t = BinaryTree(key)
            self.rightTree , t.rightTree = t, self.rightTree
	
    # * L R
    def printPreorder(self, level): 
        print(str(level*'.') + str(self.key))

        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
            
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)

    # L * R
    def printInorder(self, level): 
        if self.leftTree != None:
            self.leftTree.printInorder(level+1)

        print(str(level*'.') + str(self.key))

        if self.rightTree != None:
            self.rightTree.printInorder(level+1)

    # L R *
    def printPostorder(self, level): 
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)

        if self.rightTree != None:
            self.rightTree.printPostorder(level+1)

        print(str(level*'.') + str(self.key))
        
class BST(BinaryTree): 

	# Constructor Function
	def __init__(self,key, 
		leftTree = None, 
		rightTree = None): 
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