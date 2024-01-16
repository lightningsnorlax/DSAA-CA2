# -------------------------
# Imports
# -------------------------
from Classes.hashTable import HashTable

# -------------------------
# Initialize Function
# -------------------------
# Purpose is to make the Hash Table, statementTable, global
def initialize(): 
    global statementTable
    statementTable = HashTable(5) # Instantiate a Hash Table to store assignment statements