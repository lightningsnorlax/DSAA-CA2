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
        if globalVars.smart_cache_check:
            evaluation = globalVars.outputTable[key]
            print(f'{key}={expression}=> {int(evaluation) if evaluation != None and int(evaluation) == evaluation else evaluation}')
        else:
            # Create an instance of ParseTree
            parseTree = ParseTree(key = '?', exp = expression, ref_key=key)
            evaluation = parseTree.evaluateTree()
            if evaluation != None:
                if int(evaluation) == evaluation:
                    evaluation = int(evaluation)
            # Print evaluation without leading zeros
            print(f'{key}={expression}=> {int(evaluation) if evaluation != None and int(evaluation) == evaluation else evaluation}')