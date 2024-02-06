# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
from Classes.hashTable import HashTable

# -------------------------
# Initialize Function
# -------------------------
# Purpose is to make the Hash Table, statementTable, and other toggleable actions global
def initialize(): 
    global statementTable, brackets_check, smart_cache_check, trigo_check, logarithm_check, exp_check, referenceTable, outputTable

    statementTable = HashTable(15) # Instantiate a Hash Table to store assignment statements
    referenceTable = HashTable(15) # Instantiate a Hash Table to store reference variables
    outputTable = HashTable(15) # Instantiate a Hash Table to store output variables

    # Set Toggleable Checking Purposes
    brackets_check = False
    smart_cache_check = False
    trigo_check = False
    logarithm_check = False
    exp_check = False