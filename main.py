from Classes.controller import Controller
from Classes.general import General

def main():
    controller = Controller()
    controller.run()


if __name__ == "__main__":
    for i in General.getTextFromFile("banner.txt", "Additional Resources"):
        print(i)
    main()
    print("\nBye, thanks for using ST1507 DSAA: Assignment System Evaluator & Sorter")