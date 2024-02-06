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
    
    # When option is selected, reverse the Boolean value
    globalVars.trigo_check = not globalVars.trigo_check
    print(f"\n~ Trigonometry is now {'enabled' if globalVars.trigo_check else 'disabled'} ~\n")
    # Adjust menu option display
    action.__doc__ = f"{'Disable' if globalVars.trigo_check else 'Enable'} Trigonometry"
    
    # Check if enabled to display announcement notice
    if globalVars.trigo_check:
        # Display Banner
        file = FileHandler(folder_path = 'Additional Resources')
        for chunk in (file.readByLine("trigo_banner.txt")):
            print(chunk)