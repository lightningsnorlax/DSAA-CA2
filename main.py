# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
from Classes.controller import Controller
import Classes.globalVars as globalVars
from Classes.fileHandler import FileHandler
import math

# -------------------------
# Main Function
# -------------------------
def main():
    
    # Initialize statementTable to be global to store assignment statements
    globalVars.initialize()

    # Display Banner
    file = FileHandler(folder_path = 'Additional Resources')
    for chunk in (file.readByLine("banner.txt")):
        print(chunk)
    print("\n")
    
    # Instantiate Controller
    controller = Controller()
    controller.run()
    print("\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter")

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    main()