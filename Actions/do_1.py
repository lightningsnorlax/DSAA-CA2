# -------------------------
# Imports
# -------------------------
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Classes.globalVars as globalVars


def action():
    "Add/Modify assignment statement"
    print("do_1")

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
    print(variableName)
    print(expression)
    # Upload to Hash Table
    globalVars.statementTable[variableName] = expression

    input("\nPress enter key, to continue....\n")