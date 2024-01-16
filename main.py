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
    controller = Controller()
    controller.run()

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    globalVars.initialize() # Initialize statementTable to be global to store assignment statements
    main()