# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

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
            user_input = input(f"{input_text}")
            if condition_function(user_input, **variables):
                temp_error = False
            else:
                print(output)
        return user_input