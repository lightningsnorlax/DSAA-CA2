# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Actions.do_2 import action as action2
import time

# -------------------------
# Action Function
# -------------------------
def action():
    "Compare speeds of Smart Caching"
    print("\nComparing speeds of Option 2")
    temp_store_check = globalVars.smart_cache_check

    def timeOption2():
        start = time.time()
        action2()
        end = time.time()
        return end - start
    
    globalVars.smart_cache_check = False
    without_smart_caching = timeOption2()
    globalVars.smart_cache_check = True
    with_smart_caching = timeOption2()
    
    print("\n")
    print("-" * 30)
    print(f"Without Smart Caching: {without_smart_caching} seconds")
    print(f"With Smart Caching: {with_smart_caching} seconds")
    print(f"Difference: {without_smart_caching - with_smart_caching} seconds")
    