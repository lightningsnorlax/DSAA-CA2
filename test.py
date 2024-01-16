# Temporary main.py
# -------------------------
# Imports
# -------------------------
from Classes.controller import Controller
from Classes.general import General
import Classes.globalVars as globalVars
import Actions.do_1 as do_1
import Actions.do_2 as do_2

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
    i = 0
    for i in range(3):
        do_1.action()
    do_2.action()
    #main()