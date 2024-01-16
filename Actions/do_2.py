# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Classes.parseTree as parseTree

# -------------------------
# Action Function
# -------------------------
def action():
    "Display current assignment statements"

    print("CURRENT ASSIGNMENTS:\n********************")

    # Loop through all existing keyes in statementTable
    for key in globalVars.statementTable.getAllKeys():
        expression = globalVars.statementTable[key]
        tree = parseTree.buildParseTree(expression)
        evaluation = parseTree.evaluate(tree)
        print(f'{key}={expression}=> {evaluation}')
        
# issues to handle
# tranversal printing orders (related option 3)
# how to return integers without the decimanl points