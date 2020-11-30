from logic.LogicMain import LogicMain

class Reports:
    def __init__(self):
        self.logic = LogicMain()

    def report_options(self):
        print("1. get report \n2. see report ")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            #búa til fall sem sækir report
            pass
        elif command == "2":
            #búa til fall sem sýnir report
            pass
        else:
            print("Invalid command")