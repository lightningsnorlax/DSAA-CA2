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
    sortedKeys = globalVars.statementTable.getAllKeys()
    mergeSort.mergeSort(sortedKeys)

    # Loop through all existing keyes in statementTable
    for key in sortedKeys:
        expression = globalVars.statementTable[key]
        # Create an instance of ParseTree
        parseTree = ParseTree(key = '?', exp = expression)
        evaluation = parseTree.evaluateTree()
        print(f'{key}={expression}=> {evaluation}')
        
    print("\n")
# issues to handle
# how to return integers without the decimanl points