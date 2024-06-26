# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.general import General
from Classes.bracket_stuff import Bracketting
from Classes.smartCaching import SmartCaching

# -------------------------
# Action Function
# -------------------------
def action():
    "Add/Modify assignment statement"

    # Get user input for an assignment statement    
    statement = General.validationTracking("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n",
                                           lambda x: (len(x.split("=")) == 2 and (x.split("="))[0].isalpha()) and Bracketting(x.split("=")[1], globalVars.brackets_check).bracket_checking(),
                                           output="Invalid Expression\n")
    
    # Split statement into variable name and expression if valid
    variableName, expression = statement.split("=")

    # Overides from bracketing if check
    if globalVars.brackets_check:
        expression = Bracketting(expression, globalVars.brackets_check).parsing_exp()
        
    # Store variable name and expression into global Hash Table
    globalVars.statementTable[variableName] = expression

    # Checks if Smart Caching is toggled on
    if globalVars.smart_cache_check:
        SmartCaching(globalVars.smart_cache_check, expression, variableName).smart_cache()