# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Actions.do_2 as do_2
from Classes.fileHandler import FileHandler
from Classes.general import General
from Classes.bracket_stuff import Bracketting
from Classes.smartCaching import SmartCaching

# -------------------------
# Action Function
# -------------------------
def action():
    "Read assignment statements from file"
    
    # Instance FileHandler Object
    file = FileHandler(folder_path = 'Input')

    # Input File Validation
    inputFile = General.validationTracking("Please enter input file: ", lambda x: x.endswith(".txt"), output="Invalid File Type")

    for line in file.readByLine(inputFile):
        flag = True
        if len(line.split("=")) == 2 and line.split("=")[0].isalpha() and Bracketting(line.split("=")[1], globalVars.brackets_check).bracket_checking():
            variableName, expression = line.split("=")
            if globalVars.brackets_check:
                expression = Bracketting(expression, globalVars.brackets_check).parsing_exp()
            globalVars.statementTable[variableName] = expression     
            if globalVars.smart_cache_check:
                SmartCaching(globalVars.smart_cache_check, expression, variableName).smart_cache()
        else:
            print("Invalid File Type:", line)

    # Print out current assignments
    do_2.action()