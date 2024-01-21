# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Classes.parseTree as parseTree
import Classes.mergeSort as mergeSort

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
        tree = parseTree.buildParseTree(expression)
        evaluation = parseTree.evaluate(tree)
        print(f'{key}={expression}=> {evaluation}')
        
    print("\n")
# issues to handle
# how to return integers without the decimanl points