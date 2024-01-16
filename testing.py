import os
import importlib
from Classes.stack_new import Stack
from Classes.general import General

folderPath = "Actions"

class Controller(Stack):
    def __init__(self):
        super().__init__()
        self.__modules = []
        self.__finished_modules = []
        self.initialize_modules()

    def initialize_modules(self):
        self.push("do_")

        for file in os.listdir(folderPath):
            if file.endswith(".py") and file.startswith("do_"):
                self.__modules.append(file)
        self.__modules.sort()

    def import_module(self, file):
        module_name = file[:-3]
        return importlib.import_module(f"{folderPath}.{module_name}")

    # def recursive_test(self, files):
    #     for file in files:
    #         if file not in self.__finished_modules:
    #             module = self.import_module(file)
                
    #             sub_level_module_file = f"do_{file[3:-3]}_1.py"

    #             if sub_level_module_file in files:
    #                 self.recursive_test(list(filter(lambda x: x.startswith(f"{file[:-3]}_"), files)))

    #             else:
    #                 self.__finished_modules.append(file)
    #                 print(module.action.__doc__)
    #                 module.action()

    def generate_menu(self):
        current_modules = list(
            filter(lambda x: x.startswith(self.__str__()) and (len(x.replace(self.__str__(), "").split('_')) <= 1), self.__modules)
        )

        print(f"\n\nPlease select your choice ('{", ".join([str(num) for num in list(range(1, len(current_modules) + 1))])}'):")
        print("\n".join([f"{i+1}. {self.import_module(module).action.__doc__}" for i, module in enumerate(current_modules)]))
        if self.__str__() == "do_":
            print(f"{len(current_modules) + 1}. Exit")
        else:
            print(f"{len(current_modules) + 1}. Back")
        print("Enter choice: ", end="")

    def start(self):
        for i in General.getTextFromFile("banner.txt", "Additional Resources"):
            print(i)
        self.run()#

    def run(self):

        user_input_error = True
        while user_input_error:
            self.generate_menu()
            user_input = input()
            controller.execute(user_input)
            if self.size() <= 0:
                user_input_error = False

    def execute(self, user_input):
        filePath = os.path.join(folderPath, f"{self}{user_input}.py")
        current_modules = list(
            filter(lambda x: x.startswith(self.__str__()) and (len(x.replace(self.__str__(), "").split('_')) <= 1), self.__modules)
        )

        if f"{self}{user_input}_1.py" in self.__modules:
            self.push(f"{user_input}_")
            self.run()
        elif user_input == str(len(current_modules) + 1):
            self.pop()
        else:
            try:
                module = self.import_module(filePath[len(folderPath) + 1:])
                module.action()
            except FileNotFoundError:
                print("Method not found")
            except ModuleNotFoundError:
                print("Module not found")

controller = Controller()
# controller.generate_menu()
controller.start()