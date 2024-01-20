import Classes.globalVars as globalVars
import Actions.do_1 as do_1
import Actions.do_2 as do_2
from Classes.fileHandler import FileHandler
import Classes.mergeSort as mergeSort
from Classes.hashTable import HashTable
import Classes.parseTree as parseTree

globalVars.initialize() # Initialize statementTable to be global to store assignment statements
# Instance FileHandler Object
file = FileHandler(folder_path = 'Input')

# Input File Validation
validInputFile = False
while not validInputFile:
    inputFile = "fruits.txt"
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

for statement in message:
    # Extract variable name & expression from statement
    variableName, expression = variable_expression(statement)

    # Upload to Hash Table
    globalVars.statementTable[variableName] = expression

print(globalVars.statementTable.getAllKeys())

output_path = "output.txt"

by_result = HashTable(size=100)
printed = []
printed_none = False

with open(output_path, "w") as file:
    for key in globalVars.statementTable.getAllKeys():
        tree = parseTree.buildParseTree(globalVars.statementTable[key])
        evaluation = parseTree.evaluate(tree)
        by_result[key] = evaluation

    sorted_results = sorted(set(by_result.getAllItems()), key=lambda x: (float('-inf') if x[1] is None else x[1]), reverse=True)

    for result in sorted_results:

        if result[1] in printed:
            continue

        expressions = [(key, globalVars.statementTable[key]) for key, value in by_result.getAllItems() if value == result[1]]
        file.write(f"*** Statements with value=> {result[1]}\n")
        for key, expression in expressions:
            file.write(f"{key}={expression}\n")
        file.write("\n")

        printed.append(result[1])

