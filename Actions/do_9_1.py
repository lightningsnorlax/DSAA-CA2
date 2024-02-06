# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars

# -------------------------
# Action Function
# -------------------------
def action():
    "Enable Smart Caching"
    globalVars.smart_cache_check = not globalVars.smart_cache_check
    print(f"Smart Caching is now {'enabled' if globalVars.smart_cache_check else 'disabled'}")
    action.__doc__ = f"{'Disable' if globalVars.smart_cache_check else 'Enable'} Smart Caching"
    