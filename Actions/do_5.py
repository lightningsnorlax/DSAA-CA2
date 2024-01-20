import Classes.globalVars as globalVars
import Classes.parseTree as parseTree
import Classes.mergeSort as mergeSort
from Classes.hashTable import HashTable

def action():
    "Sort assignment statements"

    output_path = "output.txt"

    by_result = HashTable(size=100)
    printed = []

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
