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
    "Enable Logarithm"
    
    # When option is selected, reverse the Boolean value
    globalVars.logarithm_check = not globalVars.logarithm_check
    print(f"\n~ Logarithm is now {'enabled' if globalVars.logarithm_check else 'disabled'} ~\n")
    # Adjust menu option display
    action.__doc__ = f"{'Disable' if globalVars.logarithm_check else 'Enable'} Logarithm"
    
    # Check if enabled to display announcement notice
    if globalVars.logarithm_check:
        # Display Banner
        file = FileHandler(folder_path = 'Additional Resources')
        for chunk in (file.readByLine("logarithm_banner.txt")):
            print(chunk)