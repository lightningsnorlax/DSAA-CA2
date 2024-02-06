# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.bracket_stuff import Bracketting
from Classes.parseTree import ParseTree

class SmartCaching:
    def __init__(self, smart_cache_check, exp, var):
        self.__smart_cache_check = smart_cache_check
        self.__exp = exp
        self.__var = var
        
    def __reference_table_add(self, token):
        if token in globalVars.referenceTable.getAllKeys():
            globalVars.referenceTable[token].append(self.__var)
        else:
            globalVars.referenceTable[token] = [self.__var]
            
        if self.__var in globalVars.reverseReferenceTable.getAllKeys():
            globalVars.reverseReferenceTable[self.__var].append(token)
        else:
            globalVars.reverseReferenceTable[self.__var] = [token]
            
    def __output_table_add(self, eval):
        globalVars.outputTable[self.__var] = eval
        print(eval, self.__var)
        print(globalVars.outputTable.getAllItems())
        
    
    def smart_cache(self):
        bracketting = Bracketting(self.__exp, globalVars.brackets_check)
        tokens = bracketting.return_tokens()
        
        # Updates the other reference tables if updating
        if self.__var in globalVars.reverseReferenceTable.getAllKeys():
            self.__update_references()
            
        # Tokenizing
        for token in tokens:
            if token.isalpha():
                self.__reference_table_add(token)
                
        # Replacing output
        self.__add_output(self.__exp, self.__var)
        
        # Checking for need to update other output tables
        if self.__var in globalVars.referenceTable.getAllKeys():
            self.__update_output()
        
    def __add_output(self, exp, var):
        parseTree = ParseTree(key="?", exp=exp, ref_key=var)
        evaluation = parseTree.evaluateTree()
        if evaluation != None:
            if int(evaluation) == evaluation:
                evaluation = int(evaluation)
        
        self.__output_table_add(evaluation)
        
    def __update_output(self):
        print("updating output\n\n", self.__var)
        items = globalVars.referenceTable[self.__var]
        for item in items:
            self.__add_output(globalVars.statementTable[item], item)
            
    def __update_references(self):
        print("updating references")
        for ref in globalVars.reverseReferenceTable[self.__var]:
            globalVars.referenceTable[ref].remove(self.__var)