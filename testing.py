import Classes.globalVars as globalVars
import Classes.parseTree as parseTree

variableName = "a"
expression = "(1+2)"
globalVars.initialize() # Initialize statementTable to be global to store assignment statements
globalVars.statementTable[variableName] = expression

print("Please enter the variable you want to evaluate: ")
user_input = input()

if user_input in globalVars.statementTable.getAllKeys():
    print(f"\nExpression Tree: ")

    expression = globalVars.statementTable[user_input]
    tree = parseTree.buildParseTree(expression)
    evaluation = parseTree.evaluate(tree)
    tree.printInorder(0)
    print(f"Value for variable {user_input} is {evaluation}")
else:
    print(f"Variable {user_input} does not exist in the current assignment statements")