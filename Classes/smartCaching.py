# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import Classes.globalVars as globalVars
from Classes.bracket_stuff import Bracketting
from Classes.parseTree import ParseTree
import time

class SmartCaching:
    def __init__(self, smart_cache_check, exp, var):
        self.__smart_cache_check = smart_cache_check
        self.__exp = exp
        self.__var = var
        
    def __reference_table_add(self, token):
        if token in globalVars.referenceTable.getAllKeys():
            if self.__var not in globalVars.referenceTable[token]:
                globalVars.referenceTable[token].append(self.__var)
        else:
            globalVars.referenceTable[token] = [self.__var]
            
    def __output_table_add(self, eval):
        globalVars.outputTable[self.__var] = eval
    
    def smart_cache(self):
        bracketting = Bracketting(self.__exp, globalVars.brackets_check)
        tokens = bracketting.return_tokens()

        # Tokenizing
        for token in tokens:
            if token.isalpha():
                self.__reference_table_add(token)
                
        # Replacing output
        self.__add_output(self.__exp, self.__var)
        
        # Checking for need to update other output tables
        
    def __add_output(self, exp, var):
        parseTree = ParseTree(key="?", exp=exp, ref_key=var)
        evaluation = parseTree.evaluateTree()
        if evaluation != None:
            if int(evaluation) == evaluation:
                evaluation = int(evaluation)
        
        self.__output_table_add(evaluation)
        if var in globalVars.referenceTable.getAllKeys():
            self.__update_output(var)
        
    def __update_output(self, var):
        items = (globalVars.referenceTable[var]).copy()
        globalVars.referenceTable[var] = []
        count = 0
        for item in items:
            count += 1
            if item in globalVars.statementTable.getAllKeys():
                smarts = SmartCaching(globalVars.smart_cache_check, globalVars.statementTable[item], item)
                smarts.smart_cache()

    def returnVar(self):
        return self.__var, self.__exp