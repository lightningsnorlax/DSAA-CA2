# -------------------------
# Imports
# -------------------------
from Classes.controller import Controller
from Classes.general import General
import Classes.globalVars as globalVars
from Classes.fileHandler import FileHandler

# -------------------------
# Main Function
# -------------------------
def main():
    
    # Initialize statementTable to be global to store assignment statements
    globalVars.initialize()
    file = FileHandler(folder_path = 'Additional Resources')
    # Banner
    for chunk in (file.readByLine("banner.txt")):
        print(chunk, end='')
    print("\n")
    controller = Controller()
    controller.run()

# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":
    main()