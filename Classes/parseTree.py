# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.binaryTree import BinaryTree
from Classes.stack import Stack
import re

# -------------------------
# buildParseTree Function
# -------------------------
def buildParseTree(exp):
    # Tokenize Expression
	for i in ['(', '+', '-', '*', '/', ')']:
		exp = re.sub(rf'[{i}]', f' {i} ', exp) # Replace for consistent spacing in the expression
	tokens = exp.replace(' *  * ', ' ** ').split() # Join the ** operator, then split expression by spaces into elements

	stack = Stack() # Purpose of stack is to keep track of history of where it comes from
	tree = BinaryTree('?')
	stack.push(tree)

	currentTree = tree 

	for t in tokens: 
	
		# RULE 1: If token is '(' add a new node as left child 
		# and descend into that node
		if t == '(':
			currentTree.insertLeft('?') # Descend to Left
			stack.push(currentTree)
			currentTree = currentTree.getLeftTree()
		
		# RULE 2: If token is operator set key of current node 
		# to that operator and add a new node as right child 
		# and descend into that node
		elif t in ['+', '-', '*', '/', '**']:
			currentTree.setKey(t)
			currentTree.insertRight('?') # Ready for right operand
			stack.push(currentTree) # push current tree to stack to keep track of where it came from
			currentTree = currentTree.getRightTree() # descend down one level

		# RULE 3: If token is a variable name, set key of current node 
		# to that variable name and return to parent
		elif t.isalpha():
			currentTree.setKey(t)
			parent = stack.pop() # move current tree to the previous stack / parent
			currentTree = parent
		
		# RULE 4: If token is number, set key of the current node 
		# to that number and return to parent
		elif t not in ['+', '-', '*', '/', '**', ')']: 
			currentTree.setKey(float(t)) 
			parent = stack.pop() # move current tree to the previous stack / parent
			currentTree = parent
		
		# RULE 5: If token is ')' go to parent of current node
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
	op = tree.getKey() # root node

	try:
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
		else: # Check if leaf node
			try: 
				# Check if it is a variable name
				if tree.getKey().isalpha():
					variableName = tree.getKey()
					# Check if it is an existing variable name in statementTable
					if variableName in globalVars.statementTable.getAllKeys():
						expression = globalVars.statementTable[variableName]
						parseTree = buildParseTree(expression)
						return evaluate(parseTree)
					else:
						return None
			except:
				return tree.getKey()
	except:
		return None
	
# Issues to relook at
# handling of non existing variable names