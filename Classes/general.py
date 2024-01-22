# -------------------------
# Imports
# -------------------------
from pathlib import Path
import os

# -------------------------
# General Class
# -------------------------
class General:

    def __init__(self):
        pass

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
            
    @staticmethod
    # Independent of I/O
    def writeToTextToFile(file_path, text="", folder="Output", ):
        path = Path(os.path.join(folder, file_path))
        with open(path, 'w') as file:
            file.write(text)
            
    @staticmethod
    def appendTextToFile(file_path, text="", folder="Output"):
        path = Path(os.path.join(folder, file_path))
        with open(path, 'a') as file:
            file.write(text)
        
        