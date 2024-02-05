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
# Purpose is to make the Hash Table, statementTable, global
def initialize(): 
    global statementTable, brackets_check
    statementTable = HashTable(15) # Instantiate a Hash Table to store assignment statements
    brackets_check = False