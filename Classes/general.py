# -------------------------
# Imports
# -------------------------
from pathlib import Path
import os

# -------------------------
# General Class
# -------------------------
class General:

    # Constructor Function
    def __init__(self):
        pass
    
    @staticmethod
    # While loop validation
    def validationTracking(input_text, condition_function, output="Invalid Input", additional=None, **variables):
        temp_error = True
        while temp_error:
            user_input = input(f"\n{input_text}")
            if condition_function(user_input, **variables):
                temp_error = False
            else:
                print(output)
        return user_input