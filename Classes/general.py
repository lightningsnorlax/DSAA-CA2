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