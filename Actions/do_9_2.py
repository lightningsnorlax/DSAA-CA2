# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Actions.do_2 import action as action2
from Classes.smartCaching import SmartCaching
import time

# -------------------------
# Action Function
# -------------------------
def action():
    "Compare speeds of Smart Caching"
    print("\nComparing speeds of Option 2")
    print("-" * 50)
    temp_store_check = globalVars.smart_cache_check

    # Returns the time taken to execute action2
    def timeOption2():
        start = time.time()
        action2()
        end = time.time()
        return end - start
    
    # Adds to output table incase its users first interaction with the program
    globalVars.smart_cache_check = False
    without_smart_caching = timeOption2()
    globalVars.smart_cache_check = True
    if globalVars.smart_cache_check:
        for key in globalVars.statementTable.getAllKeys():
            expression = globalVars.statementTable[key]
            SmartCaching(globalVars.smart_cache_check, expression, key).smart_cache()

    # Runs with smart caching
    with_smart_caching = timeOption2()
    
    # Printing
    print("\n")
    print("Speed Comparison")
    print("-" * 50)
    print(f"Without Smart Caching: {without_smart_caching:.10f} seconds")
    print(f"With Smart Caching: {with_smart_caching:.10f} seconds")
    print(f"Difference: {without_smart_caching - with_smart_caching:.10f} seconds")
    globalVars.smart_cache_check = temp_store_check
    