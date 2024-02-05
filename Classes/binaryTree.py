# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

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
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)

        if type(self.key) == float and int(self.key) == float(self.key):
            print(str(level*'.') + str(int(self.key)))
        else:
            print(str(level*'.') + str(self.key))

        if self.leftTree != None:
            self.leftTree.printInorder(level+1)

    # L R *
    def printPostorder(self, level): 
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)

        if self.rightTree != None:
            self.rightTree.printPostorder(level+1)

        print(str(level*'.') + str(self.key))