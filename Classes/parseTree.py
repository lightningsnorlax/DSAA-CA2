# -------------------------
# Imports
# -------------------------
from binaryTree import BinaryTree
from stack import Stack
import re

# -------------------------
# Build Parse Tree Function
# -------------------------
def buildParseTree(exp):
    # Tokenize Expression
	for i in ['(', '+', '-', '*', '/', ')']:
		exp = re.sub(rf'[{i}]', f' {i} ', exp) # Replace for consistent spacing in the expression
	tokens = exp.replace(' *  * ', ' ** ').split() # Join the ** operator, then split expression by spaces into elements

	stack = Stack()
	tree = BinaryTree('?')
	stack.push(tree)

	currentTree = tree 

	for t in tokens: 
	
		# RULE 1: If token is '(' add a new node as left child 
		# and descend into that node
		if t == '(':
			currentTree.insertLeft('?') 
			stack.push(currentTree)
			currentTree = currentTree.getLeftTree()
		
		# RULE 2: If token is operator set key of current node 
		# to that operator and add a new node as right child 
		# and descend into that node
		elif t in ['+', '-', '*', '/', '**']:
			currentTree.setKey(t)
			currentTree.insertRight('?') 
			stack.push(currentTree)
			currentTree = currentTree.getRightTree() 
		
		# RULE 3: If token is number, set key of the current node 
		# to that number and return to parent
		elif t not in ['+', '-', '*', '/', '**', ')'] : 
			currentTree.setKey(float(t))
			parent = stack.pop()
			currentTree = parent
		
		# RULE 4: If token is ')' go to parent of current node
		elif t == ')':
			currentTree = stack.pop()
		
		else:
			raise ValueError

	return tree

# ----------------------------
# Evaluate Parse Tree Function
# ----------------------------
def evaluate(tree):
	leftTree = tree.getLeftTree()
	rightTree = tree.getRightTree()
	op = tree.getKey()

	if leftTree != None and rightTree != None: 
		if op == '+':
			return evaluate(leftTree) + evaluate(rightTree)
		elif op == '-':
			return evaluate(leftTree) - evaluate(rightTree)
		elif op == '*':
			return evaluate(leftTree) * evaluate(rightTree)
		elif op == '/':
			return evaluate(leftTree) / evaluate(rightTree)
		elif op == '**':
			return evaluate(leftTree) ** evaluate(rightTree)
	else:
		return tree.getKey()