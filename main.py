# -------------------------
# Imports
# -------------------------
from Classes.controller import Controller
from Classes.general import General
import Classes.globalVars as globalVars

# -------------------------
# Main Function
# -------------------------
def main():
    # Initialize statementTable to be global to store assignment statements
    globalVars.initialize()
    
    # Banner
    for chunk in (General.getTextFromFile("banner.txt", folder="Additional Resources")):
        print(chunk, end='')
    print("\n")
    controller = Controller()
    controller.run()

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    main()