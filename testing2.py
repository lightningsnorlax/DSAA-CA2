import Classes.globalVars as globalVars
import Classes.parseTree as parseTree
import Classes.mergeSort as mergeSort
from Classes.parseTree import ParseTree

globalVars.initialize()

def variable_expression(assigmentStatement):
    # Extract Variable Name
    variableName, expression = assigmentStatement.split("=")
    return variableName, expression

# Get user input for an assignment statement
statement = "a=(1+2)"

# Extract variable name & expression from statement
variableName, expression = variable_expression(statement)

# Upload to Hash Table
globalVars.statementTable[variableName] = expression
    
# Action 3
print("Please enter the variable you want to evaluate: ")
user_input = "a"

if user_input in globalVars.statementTable.getAllKeys():
    print(f"\nExpression Tree: ")

    parseTree = ParseTree(key='?', exp=expression)
    evaluation = parseTree.evaluateTree()
    parseTree.printInorder(0)
    print(f'Value for variable "{user_input}" is {evaluation}')
else:
    print(f"Variable {user_input} does not exist in the current assignment statements")

