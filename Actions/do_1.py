# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars

# -------------------------
# Action Function
# -------------------------
def action():
    "Add/Modify assignment statement"

    # ----------------------------
    # variable_expression Function
    # ----------------------------
    # Function to extract variable name & expression from assignment statement
    def variable_expression(assigmentStatement):
        # Extract Variable Name
        variableName, expression = assigmentStatement.split("=")
        return variableName, expression
    
    # Get user input for an assignment statement
    statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")

    # Extract variable name & expression from statement
    variableName, expression = variable_expression(statement)

    # Upload to Hash Table
    globalVars.statementTable[variableName] = expression

    input("\nPress enter key, to continue....\n")

# issues to take note of
# index out of range when variable name is 'e'