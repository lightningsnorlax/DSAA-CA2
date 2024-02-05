# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import re
from Classes.stack import Stack
from Classes.binaryTree import BinaryTree
# from Classes.parseTree import buildParseTree, evaluate
from Classes.parseTree import ParseTree
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
        
        parseTree = ParseTree(key='?', exp=expression)
        evaluation = parseTree.evaluateTree()
        parseTree.printInorder(0)
        
        if int(evaluation) == evaluation:
            evaluation = int(evaluation)
        print(f'Value for variable "{user_input}" is {evaluation}')
    else:
        print(f"Variable {user_input} does not exist in the current assignment statements")

# issues to handle
# tranversal printing orders