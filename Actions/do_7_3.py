# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.fileHandler import FileHandler

# -------------------------
# Action Function
# -------------------------
def action():
    "Enable Exponential"
    
    globalVars.exp_check = not globalVars.exp_check
    print(f"\n~ Exponential is now {'enabled' if globalVars.exp_check else 'disabled'} ~\n")
    action.__doc__ = f"{'Disable' if globalVars.exp_check else 'Enable'} Exponential"
    
    if globalVars.exp_check:
        # Display Banner
        file = FileHandler(folder_path = 'Additional Resources')
        for chunk in (file.readByLine("exp_banner.txt")):
            print(chunk)