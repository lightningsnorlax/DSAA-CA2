# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# ------------------
# Imports
# ------------------
import os

# ------------------
# FileHandler Class
# ------------------
class FileHandler:
    """A class for handling reading & writing of files."""
    # Constructor Function
    def __init__(self, folder_path):
        # if folder_path is not provided, use current working directory
        self.__folder_path = folder_path or os.getcwd()

    # Read File Names From Folder
    def readFromFolder(self):
        try:
            files = os.listdir(self.__folder_path) # store list of file names
            return files
        except FileNotFoundError:
            print(f"Folder not found: {self.__folder_path}")
            return []

    # Read line by line from File
    def readByLine(self, file_name):
        file_path = os.path.join(self.__folder_path, file_name)
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    # not stored in memory
                    yield line.strip() # strip trailing newline character
        except FileNotFoundError:
            print(f"File {file_name} not found in {self.__folder_path} folder")
            return None

    # Write to File
    def writeToFile(self, output_folder_path, output_file_name, msg):
        file_path = os.path.join(output_folder_path, output_file_name)
        try:
            with open(file_path, 'w') as file:
                file.write(msg) # write to new txt file
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")
            
    # Add to File (w/o overwritting)
    def appendToFile(self, output_folder_path, output_file_name, msg):
        file_path = os.path.join(output_folder_path, output_file_name)
        try:
            with open(file_path, 'a') as file:
                file.write(msg)
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")