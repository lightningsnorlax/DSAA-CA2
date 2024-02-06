# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import os
import importlib
from Classes.stack import Stack

# Set Folder Path to access files to perform the respective menu option's actions
folderPath = "Actions"

# -------------------------
# Controller Class
# -------------------------
class Controller(Stack):

    # Constructor Function
    def __init__(self):
        super().__init__()
        self.__modules = []
        self.__finished_modules = []
        self.__initialize_modules()

    # Set up modules
    def __initialize_modules(self):
        self.push("do_")

        for file in os.listdir(folderPath):
            if file.endswith(".py") and file.startswith("do_"):
                self.__modules.append(file)
        self.__modules.sort()

    # Importing the action from file
    def __import_module(self, file):
        module_name = file[:-3]
        return importlib.import_module(f"{folderPath}.{module_name}")

    # Dynamic menu generation
    def __generate_menu(self):
        # Get current existing modules from 'Action' Folder
        current_modules = list(filter(lambda x: x.startswith(self.__str__()) and (len(x.replace(self.__str__(), "").split('_')) <= 1), self.__modules))

        print("\nPlease select your choice ('{}'): ".format("','".join(map(str, range(1, len(current_modules) + 2)))))
        # Print Menu Options
        print("\n".join([f"\t{i+1}. {self.__import_module(module).action.__doc__}" for i, module in enumerate(current_modules)]))

        # Exit if lowest level, otherwise go back
        if self.__str__() == "do_":
            print(f"\t{len(current_modules) + 1}. Exit")
        else:
            print(f"\t{len(current_modules) + 1}. Back")
        print("Enter choice: ", end="")

    # Run the menu
    def run(self):
        user_input_error = True

        while user_input_error:
            # Display Menu
            self.__generate_menu()
            # Get user option
            user_input = input()
            # Execute option
            self.__execute(user_input)
            if self.size() <= 0:
                user_input_error = False

    # Attempting to execute the function under a file
    def __execute(self, user_input):
        filePath = os.path.join(folderPath, f"{self}{user_input}.py")
        current_modules = list(filter(lambda x: x.startswith(self.__str__()) and (len(x.replace(self.__str__(), "").split('_')) <= 1), self.__modules))

        # If user chooses a valid integer option
        if f"{self}{user_input}_1.py" in self.__modules:
            self.push(f"{user_input}_")
            self.run()
        # If user chooses the 'Exit' Option
        elif user_input == str(len(current_modules) + 1):
            self.pop()
        else:
            try:
                module = self.__import_module(filePath[len(folderPath) + 1:])
                module.action()
                input("\nPress enter key, to continue....")
            # If user chooses an invalid option
            except FileNotFoundError:
                print("Option does not exist!")
            except ModuleNotFoundError:
                print("Invalid option!")