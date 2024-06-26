# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.smartCaching import SmartCaching

# -------------------------
# Action Function
# -------------------------
def action():
    "Enable Smart Caching"
    
    # Toggling the check
    globalVars.smart_cache_check = not globalVars.smart_cache_check

    # Changing docstring
    print(f"Smart Caching is now {'enabled' if globalVars.smart_cache_check else 'disabled'}")
    action.__doc__ = f"{'Disable' if globalVars.smart_cache_check else 'Enable'} Smart Caching"

    # Run all outputs in case its the user's first interaction with the program
    if globalVars.smart_cache_check:
        for key in globalVars.statementTable.getAllKeys():
            expression = globalVars.statementTable[key]
            SmartCaching(globalVars.smart_cache_check, expression, key).smart_cache()
    