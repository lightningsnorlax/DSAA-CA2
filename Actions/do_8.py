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
    "Enable Smart Bracketing System"
    globalVars.brackets_check = not globalVars.brackets_check
    print(f"Smart Bracketing System is now {'enabled' if globalVars.brackets_check else 'disabled'}")
    action.__doc__ = f"{'Disable' if globalVars.brackets_check else 'Enable'} Smart Bracketing System"
