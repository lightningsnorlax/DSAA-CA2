# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Classes.mergeSort as mergeSort
from Classes.parseTree import ParseTree

# -------------------------
# Action Function
# -------------------------
def action():
    "Display current assignment statements"

    print("\nCURRENT ASSIGNMENTS:\n********************")

    # Sort statements in alphabetical order, according to variable name (key)
    sortedKeys = mergeSort.mergeSort(globalVars.statementTable.getAllKeys())

    # Loop through all existing keyes in statementTable
    for key in sortedKeys:
        expression = globalVars.statementTable[key]
        # Create an instance of ParseTree
        parseTree = ParseTree(key = '?', exp = expression)
        evaluation = parseTree.evaluateTree()
        # Print evaluation without leading zeros
        print(f'{key}={expression}=> {int(evaluation) if int(evaluation) == evaluation else evaluation}')