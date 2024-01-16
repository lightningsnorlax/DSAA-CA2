# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars

# -------------------------
# Action Function
# -------------------------
def action():
    "Display current assignment statements"
    print("do_2")

    for key in globalVars.statementTable.getAlKeys():
        # access the key
        # evaluate the key
        # print out / return in a list

    keys_list = globalVars.statementTable.getAllItems()
    print(keys_list)