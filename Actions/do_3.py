# -------------------------
# Imports
# -------------------------
import re
from Classes.stack import Stack
from Classes.binaryTree import BinaryTree
# from Classes.parseTree import buildParseTree, evaluate
import Classes.parseTree as parseTree
import Classes.globalVars as globalVars

# -------------------------
# Action Function
# -------------------------
def action():
    "Evaluate a single variable"
    # And print parse tree

    print("Please enter the variable you want to evaluate: ")
    user_input = input()

    if user_input in globalVars.statementTable.getAllKeys():
        print(f"\nExpression Tree: ")

        expression = globalVars.statementTable[user_input]
        tree = parseTree.buildParseTree(expression)
        evaluation = parseTree.evaluate(tree)
        tree.printInorder(0)
        print(f'Value for variable "{user_input}" is {evaluation}')
    else:
        print(f"Variable {user_input} does not exist in the current assignment statements")

# issues to handle
# tranversal printing orders