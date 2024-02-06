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

    # Get output file
    output_path = General.validationTracking("\nPlease enter output file: ", lambda x: x.endswith(".txt"), output="Invalid File Type")

    # Set Hash Table for output
    by_result = HashTable(50)
    printed = []
    
    # Instanitate FileHandler class
    file = FileHandler(folder_path = 'Output')
    file.writeToFile(output_path, "")

    # Run output if check is on
    if globalVars.smart_cache_check:
        for key in globalVars.outputTable.getAllKeys():
            by_result[key] = globalVars.outputTable[key]
    # Having to run all evaluations because no check
    else:
        for key in globalVars.statementTable.getAllKeys():
            parseTree = ParseTree(key='?', exp=globalVars.statementTable[key])
            evaluation = parseTree.evaluateTree()
            by_result[key] = evaluation

    # Sort according to the value of the key, set None as the lowest possible value for sorting purpose
    sorted_results = sorted(set(by_result.getAllItems()), key=lambda x: (float('-inf') if x[1] is None else x[1]), reverse=True)

    # Print out the sorted results
    for result in sorted_results:
        expressions = [(key, globalVars.statementTable[key]) for key, value in by_result.getAllItems() if value == result[1]]
        # Sort keys in order of alphabet
        sorted_expression_keys = mergeSort.mergeSort([key for key, _ in expressions])
        # Print value, removed leading zeros
        file.appendToFile(output_folder_path = 'Output', output_file_name = output_path, msg = f"*** Statements with value=> {int(result[1]) if result[1]!= None and int(result[1]) == result[1] else result[1]}\n")
        
        # Add corresponding variables with that value
        for key in sorted_expression_keys:
            # Find matching key-value in expressions list
            expression_value = next((value for k, value in expressions if k == key), None)
            # Add line to file
            file.appendToFile(output_folder_path = 'Output', output_file_name = output_path, msg = f"{key}={expression_value}\n")
        file.appendToFile(output_folder_path = 'Output', output_file_name = output_path, msg = "\n")

        printed.append(result[1])