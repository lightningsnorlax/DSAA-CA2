# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
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

    # Check if user requested variable exists
    if user_input in globalVars.statementTable.getAllKeys():
        print(f"\nExpression Tree: ")

        # Obtain variable's assignment statement
        expression = globalVars.statementTable[user_input]
        
        # Instantiate ParseTree
        parseTree = ParseTree(key='?', exp=expression)
        # Evaluate ParseTree
        evaluation = parseTree.evaluateTree()
        # Print in order
        parseTree.printInorder(0)

        # Print without leading zeros
        print(f'Value for variable "{user_input}" is {int(evaluation) if int(evaluation) == evaluation else evaluation}')
    else:
        # User requested variable does not exist
        print(f"Variable {user_input} does not exist in the current assignment statements")