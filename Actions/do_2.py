# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.parseTree import ParseTree
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
        # parseTree = ParseTree(key='?')
        # tree = parseTree.buildParseTree(expression)
        # evaluation = parseTree.evaluate(tree)
        parseTree = ParseTree(key = '?', exp = expression)
        evaluation = parseTree.evaluateTree()
        print(f'{key}={expression}=> {evaluation}')
# issues to handle
# how to return integers without the decimanl points