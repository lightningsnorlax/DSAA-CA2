# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
from Classes.parseTree import ParseTree
import Classes.globalVars as globalVars
from Classes.fileHandler import FileHandler

# -------------------------
# Action Function
# -------------------------
def action():
    "Visualize assignment statement as Parse Tree"

    # Display Banner
    file = FileHandler(folder_path = 'Additional Resources')
    for chunk in (file.readByLine("visualization_banner.txt")):
        print(chunk)
        
    print("\nPlease enter the variable you want to visualize as a Parse Tree: ")
    user_input = input()

    # Check if user requested variable exists
    if user_input in globalVars.statementTable.getAllKeys():
        # Obtain variable's assignment statement
        expression = globalVars.statementTable[user_input]
        
        # Instantiate ParseTree
        parseTree = ParseTree(key='?', exp=expression)
        # Draw ParseTree
        parseTree.drawParseTree(variableName = user_input)
    else:
        # User requested variable does not exist
        print(f"Variable {user_input} does not exist in the current assignment statements")