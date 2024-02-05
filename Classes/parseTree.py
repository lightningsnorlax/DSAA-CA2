# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.binaryTree import BinaryTree
from Classes.stack import Stack
import re
import operator
import turtle
import tkinter as tk
import time

# -------------------------
# ParseTree Class
# -------------------------
class ParseTree(BinaryTree):

	# Constructor Function
	def __init__(self, key='?', exp = None, leftTree=None, rightTree=None):
		super().__init__(key, leftTree, rightTree)
		self.exp = exp

	def __buildParseTree(self):
		# Tokenize Expression
		for i in ['(', '+', '-', '*', '/', ')']:
			self.exp = re.sub(rf'[{i}]', f' {i} ', self.exp) # Replace for consistent spacing in the expression
		tokens = self.exp.replace(' *  * ', ' ** ').split() # Join the ** operator, then split expression by spaces into elements

		stack = Stack() # Purpose of stack is to keep track of history of where it comes from
		tree = self
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

	def evaluateTree(self):
		tree = self.__buildParseTree()
		return self.__evaluate(tree)
	
	def __evaluate(self, tree):
		# Source Credits: https://runestone.academy/ns/books/published/pythonds/Trees/ParseTree.html
		operators = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv, '**' : operator.pow}
		
		leftTree = tree.getLeftTree()
		rightTree = tree.getRightTree()

		try:
			if leftTree != None and rightTree != None:
				function = operators[tree.getKey()] # root node to get operator
				return function(self.__evaluate(leftTree), self.__evaluate(rightTree))
			else: # Check if leaf node
				try: 
					# Check if it is a variable name
					if tree.getKey().isalpha():
						variableName = tree.getKey()
						# Check if it is an existing variable name in statementTable
						if variableName in globalVars.statementTable.getAllKeys():
							expression = globalVars.statementTable[variableName]
							parseTree = ParseTree(key = '?', exp = expression)
							return parseTree.evaluateTree()
						else:
							return None
				except:
					return tree.getKey()
		except:
			return None

	def drawParseTree(self):
		# Referenced Source Code Credits: https://gist.github.com/Liwink/b81e726ad89df8b0754a3a1d0c40d0b4
		def _convertToDrawString(tree):
			if tree is None:
				return 'null'
			if isinstance(tree.key, float):
				return str(tree.key)
			if tree.key.isalpha():
				return tree.key
			return f'[{tree.key} {_convertToDrawString(tree.leftTree)} {_convertToDrawString(tree.rightTree)}]'
		
		def on_screen_click(x, y):
			print(f"Screen clicked at coordinates ({x}, {y})")
            # You can implement redirection logic or any other action here
		
		def _draw(node, x, y, dx):
			if node:
				t.goto(x, y)
				t.penup()
				t.goto(x, y-20)
				t.pendown()

				t.write(str(node.key), align='center', font=('Arial', 12, 'normal'))

				_draw(node.leftTree, x-dx, y-60, dx)

				t.penup()
				t.goto(x, y-20)
				t.pendown()
				
				_draw(node.rightTree, x+dx, y-60, dx)

		draw_string = _convertToDrawString(self.__buildParseTree())

		# Set up turtle window with a minimum width and height
		min_width = 300
		min_height = 300
		turtle_width = max(len(draw_string) * 10, min_width) # Adjust factor accordingly
		turtle_height = max(300, min_height)

		# Set up Tkinter window
		root = tk.Tk()
		root.geometry(f'{turtle_width}x{turtle_height}-5+40')  # Adjust window size and position as needed
		cv = turtle.ScrolledCanvas(root, width=900, height=900)
		cv.pack()
		screen = turtle.TurtleScreen(cv)
		screen.screensize(2000, 1500)
		t = turtle.RawTurtle(screen)
		t.hideturtle()

		t.speed(0)

		t.penup()
		t.goto(0, 30 * 2)

		_draw(self, 0, 30 * 2, 35 * 2)

		# Bind the click event to the screen
		screen.onclick(on_screen_click)

		root.mainloop()