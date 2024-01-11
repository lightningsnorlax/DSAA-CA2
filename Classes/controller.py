from Classes.general import General

class Controller:

    @staticmethod
    def do_1():
        "Add/Modify assignment statement"
        print("Doing 1")

    @staticmethod
    def do_2():
        "Display current assignment statements"
        print("Doing 2")

    @staticmethod
    def do_3():
        "Evaluate a single variable"
        print("Doing 3")

    @staticmethod
    def do_4():
        "Read assignment statements from file"
        print("Doing 4")

    @staticmethod
    def do_5():
        "Sort assignment statements"
        print("Doing 5")

    @staticmethod
    def do_6():
        "Exit"
        print("\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter")

    @staticmethod
    def execute(user_input):
        controller_name = f"do_{user_input}"
        try:
            controller = getattr(Controller, controller_name)
        except AttributeError:
            print("Method not found")
        else:
            controller()

    @staticmethod
    def run():
        for i in General.getTextFromFile("banner.txt", "Additional Resources"):
            print(i)
        user_input = 0
        while(user_input != "6"):
            Controller.generate_menu()
            user_input = (input())
            Controller.execute(user_input)

    @staticmethod
    # Generate menu passed on existing functions that start with do_
    def generate_menu():
        do_methods = [m for m in dir(Controller) if m.startswith('do_')]
        print(f"\n\nPlease select your choice ('{"','".join([method[-1] for method in do_methods])}'):")
        menu_string = "\n".join(
            [f"{method[-1]}. {getattr(Controller, method).__doc__}"
             for method in do_methods])
        print(menu_string)
        print("Enter choice: ", end="")

