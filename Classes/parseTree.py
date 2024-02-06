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
import functools

# -------------------------
# ParseTree Class
# -------------------------
class ParseTree(BinaryTree):

	# Constructor Function
	def __init__(self, key='?', exp = None, leftTree=None, rightTree=None, ref_key=None):
		super().__init__(key, leftTree, rightTree)
		self.exp = exp
		self.__ref_key = ref_key

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
		# Referenced Source Credits: https://runestone.academy/ns/books/published/pythonds/Trees/ParseTree.html
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
						if variableName == self.__ref_key:
							return None
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

	def drawParseTree(self, variableName):
		# Function to get the node value at the clicked position
		def get_clicked_node_value(x, y, tree):
			# Function to calculate the Euclidean distance between two points
			def distance(x1, y1, x2, y2):
				return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

			# Helper function to traverse the tree and find the closest node
			def find_closest_node(node, target_x, target_y):
				if node is None:
					return None, float('inf')  # Return None if node is None and infinity as initial distance

				# Get the position of the current node
				current_x, current_y = node.position

				# Calculate the distance between the current node and the clicked position
				current_distance = distance(current_x, current_y, target_x, target_y)

				# Recursively find the closest node in the left and right subtrees
				left_node, left_distance = find_closest_node(node.leftTree, target_x, target_y)
				right_node, right_distance = find_closest_node(node.rightTree, target_x, target_y)

				# Compare distances and return the closest node
				if current_distance < left_distance and current_distance < right_distance:
					return node, current_distance
				elif left_distance < right_distance:
					return left_node, left_distance
				else:
					return right_node, right_distance

			# Initialize the starting node as the root of the tree
			starting_node = self

			# Call the helper function to find the closest node
			closest_node, closest_distance = find_closest_node(starting_node, x, y)

			# Return the value of the closest node
			return closest_node.key if closest_node else None

		# Referenced Source Code Credits: https://gist.github.com/Liwink/b81e726ad89df8b0754a3a1d0c40d0b4
		def _convertToDrawString(tree):
			if tree is None:
				return 'null'
			if isinstance(tree.key, float):
				return str(tree.key)
			if tree.key.isalpha():
				return tree.key
			return f'[{tree.key} {_convertToDrawString(tree.leftTree)} {_convertToDrawString(tree.rightTree)}]'
		
		def _on_screen_click(x, y, tree):
			node_value = get_clicked_node_value(x, y, tree)
			try:
				if str(node_value).isalpha():
					expression = globalVars.statementTable[node_value]
				
					# Instantiate ParseTree
					parseTree = ParseTree(key='?', exp=expression)
					# Draw ParseTree
					parseTree.drawParseTree(node_value)
			except:
				pass

		# Draw
		def _draw(node, x, y, dx, forward_color='blue', backward_color='red'):
			if node:
				t.goto(x, y)
				t.penup()
				t.goto(x, y - 20)
				t.pendown()

				if str(node.key).isalpha():
					tree = ParseTree(key='?', exp=globalVars.statementTable[str(node.key)])
					evaluation = tree.evaluateTree()
					text = f'{node.key} = {evaluation}'
				else:
					text = str(node.key)

				t.pencolor(forward_color)
				t.write(text, align='center', font=('Arial', 12, 'bold'))

				# Add the position attribute to the node for later use
				node.position = (x, y)

				_draw(node.leftTree, x - dx, y - 60, dx, forward_color = 'blue', backward_color = 'orange')

				t.penup()
				t.goto(x, y - 20)
				t.pendown()

				_draw(node.rightTree, x + dx, y - 60, dx, forward_color = 'blue', backward_color = 'green')

				# Draw backward after drawing the tree forward
				t.penup()
				t.goto(x, y - 20)
				t.pencolor(backward_color)
				t.pendown()
				t.backward(20)  # Adjust this value as needed

		draw_string = _convertToDrawString(self.__buildParseTree())

		# Set up turtle window with a minimum width and height
		turtle_width = max(len(draw_string) * 10, 300) # Adjust factor accordingly
		turtle_height = 300

		# Referenced Source Code Credits: https://stackoverflow.com/questions/14730475/python-turtle-window-with-scrollbars
		# Set up Tkinter window
		root = tk.Tk()
		root.geometry(f'{turtle_width}x{turtle_height}-5+50')  # Move window position to left end of PC screen

		cv = turtle.ScrolledCanvas(root, width=900, height=900)
		cv.pack()

		screen = turtle.TurtleScreen(cv)
		screen.screensize(2000, 1500)

		t = turtle.RawTurtle(screen)
		t.hideturtle()
		t.speed(1)
		t.pensize(3)

		t.penup()
		t.goto(0, 70)
		t.pendown()
		t.color('red')
		tree = ParseTree(key='?', exp=globalVars.statementTable[variableName])
		evaluation = tree.evaluateTree()
		t.write(f'{variableName} = {evaluation}', align='center', font=('Arial', 15, 'bold'))
		
		t.penup()
		t.color('black')
		# Commence drawing
		_draw(self, 0, 30 * 2, 35 * 2, forward_color='blue', backward_color='red')

		# Bind the click event to the screen using a lambda function
		screen.onclick(functools.partial(_on_screen_click, tree=self))

		root.mainloop()