# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.parseTree import ParseTree
import Classes.mergeSort as mergeSort
from Classes.hashTable import HashTable
from Classes.general import General
from Classes.fileHandler import FileHandler

# -------------------------
# Action Function
# -------------------------
def action():
    "Sort assignment statements"
    # By their value (in descending order), followed by alphabetically order by variable name
    # Sorted results will be written back to an output file

    output_path = General.validationTracking("Please enter output file: ", lambda x: x.endswith(".txt"))

    by_result = HashTable(size=100)
    printed = []
    
    file = FileHandler(folder_path = 'Output')
    file.writeToFile(output_path, "")
    
    for key in globalVars.statementTable.getAllKeys():
        parseTree = ParseTree(key='?', exp=globalVars.statementTable[key])
        evaluation = parseTree.evaluateTree()
        by_result[key] = evaluation

    sorted_results = sorted(set(by_result.getAllItems()), key=lambda x: (float('-inf') if x[1] is None else x[1]), reverse=True)

    for result in sorted_results:

        if result[1] in printed:
            continue

        expressions = [(key, globalVars.statementTable[key]) for key, value in by_result.getAllItems() if value == result[1]]
        file.appendToFile(output_path, f"*** Statements with value=> {result[1]}\n")
        for key, expression in expressions:
            file.appendToFile(output_path, f"{key}={expression}\n")
        file.appendToFile(output_path, "\n")

        printed.append(result[1])