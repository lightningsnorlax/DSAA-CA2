# ------------------
# Imports
# ------------------
from pathlib import Path
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
        self.__msg = None # to store content from file

    # Read File Names From Folder
    def readFromFolder(self):
        files = os.listdir(self.__folder_path) # store list of file names
        return files

    # Read From File
    def readFromFile(self, file_name):
        file_path = os.path.join(self.__folder_path, file_name)
        with open(file_path, 'r') as file:
            self.__msg = file.read().splitlines() # read & store txt file with multiple lines in a list
            return self.__msg
        
    # Getter to provide indirect access to self.__msg
    def getMsg(self):
        return self.__msg

    # Write to File
    def writeToFile(self, output_folder_path, output_file_name, msg):
        file_path = os.path.join(output_folder_path, output_file_name)
        with open(file_path, 'w') as file:
            file.write(msg) # write to new txt file
            
    def appendToFile(self, output_folder_path, output_file_name, msg):
        file_path = os.path.join(output_folder_path, output_file_name)
        with open(file_path, 'a') as file:
            file.write(msg)
            
    def readByLine(self, file_name):
        file_path = os.path.join(self.__folder_path, file_name)
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    yield line
        except FileNotFoundError:
            print(f"File {file_name} not found in {self.__folder_path} folder")

    # ------------------
    # For Reference
    # ------------------
    @staticmethod
    # Independent of I/O
    def getTextFromFile(file_path, folder="Input", chunk_size=1024):
        path = Path(os.path.join(folder, file_path))
        print(path)
        try:
            with open(path, 'r') as file:
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk
        except FileNotFoundError:
            print(f"File {file_path} not found in {folder} folder")