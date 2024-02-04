# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Actions.do_2 as do_2
from Classes.fileHandler import FileHandler
from Classes.general import General
from Classes.bracket_stuff import Bracketting

# -------------------------
# Action Function
# -------------------------
def action():
    "Read assignment statements from file"
    
    # Instance FileHandler Object
    file = FileHandler(folder_path = 'Input')

    # Input File Validation
    inputFile = General.validationTracking("Please enter input file: ",
                                           lambda x: x.endswith(".txt"))

    for line in file.readByLine(inputFile):
        if Bracketting(line, False).bracket_checking():
            variableName, expression = line.split("=")
            globalVars.statementTable[variableName] = expression
        else:
            print("Invalid expression:", line)

    # Print out current assignments
    do_2.action()