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
    "Enable Trigonometry"
    
    globalVars.trigo_check = not globalVars.trigo_check
    print(f"\n~ Trigonometry is now {'enabled' if globalVars.trigo_check else 'disabled'} ~\n")
    action.__doc__ = f"{'Disable' if globalVars.trigo_check else 'Enable'} Trigonometry"
    
    if globalVars.trigo_check:
        # Display Banner
        file = FileHandler(folder_path = 'Additional Resources')
        for chunk in (file.readByLine("trigo_banner.txt")):
            print(chunk)