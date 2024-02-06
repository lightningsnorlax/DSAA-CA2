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
    
    # When option is selected, reverse the Boolean value
    globalVars.exp_check = not globalVars.exp_check
    print(f"\n~ Exponential is now {'enabled' if globalVars.exp_check else 'disabled'} ~\n")
    # Adjust menu option display
    action.__doc__ = f"{'Disable' if globalVars.exp_check else 'Enable'} Exponential"
    
    # Check if enabled to display announcement notice
    if globalVars.exp_check:
        # Display Banner
        file = FileHandler(folder_path = 'Additional Resources')
        for chunk in (file.readByLine("exp_banner.txt")):
            print(chunk)