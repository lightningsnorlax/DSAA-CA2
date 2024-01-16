# -------------------------
# Imports
# -------------------------
from Classes.hashTable import HashTable

# -------------------------------------------------
# Initialize Function to make statementTable global
# -------------------------------------------------
def initialize(): 
    global statementTable
    statementTable = HashTable(5) # Instantiate a Hash Table to store assignment statements