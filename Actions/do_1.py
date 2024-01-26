# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.general import General
from Classes.bracket_stuff import Bracketting

# -------------------------
# Action Function
# -------------------------
def action():
    "Add/Modify assignment statement"

    # Get user input for an assignment statement    
    statement = General.validationTracking("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n",
                                           lambda x: (len(x.split("=")) == 2 and (x.split("="))[0].isalpha()) and Bracketting(x.split("=")[1], False).bracket_checking(),
                                           output="error, Ya entered smt wrong m8")
    variableName, expression = statement.split("=")
    globalVars.statementTable[variableName] = expression