# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
import Actions.do_1 as do_1
import Actions.do_2 as do_2
from Classes.fileHandler import FileHandler

def action():
    "Read assignment statements from file"
    
    # Instance FileHandler Object
    file = FileHandler(folder_path = 'Input')

    # Input File Validation
    validInputFile = False
    while not validInputFile:
        inputFile = input(f'Please enter input file: ')
        if inputFile[-4:] == ".txt":
            try:
                # Attempt to read from file
                file.readFromFile(inputFile)
                message = file.getMsg()
                # # Check if content of file is empty
                # if not message or message.isspace():
                #     print('The file content is empty or contains only whitespaces. You may want to check and try again.')
                #     validInputFile = False
                # else:
                validInputFile = True
            except FileNotFoundError:
                print("File does not exist! Please check that it's in the Input Folder.")
                validInputFile = False
        else: # Incorrect file type
            print('Invalid File Type! Please re-enter only .txt format files.')
            validInputFile = False

    # Function to extract variable name & expression from assignment statement
    def variable_expression(assigmentStatement):
        # Extract Variable Name
        variableName, expression = assigmentStatement.split("=")
        return variableName, expression

    # Loop through list of statements
    for statement in message:
        # Extract variable name & expression from statement
        variableName, expression = variable_expression(statement)

        # Upload to Hash Table
        globalVars.statementTable[variableName] = expression

    # Print out current assignments
    do_2.action()