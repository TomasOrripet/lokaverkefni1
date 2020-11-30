from logic.LogicMain import LogicMain

class Destinations:
    def __init__(self):
        self.logic = LogicMain()

    def destination_options(self):
        print("1. get destination info \n2. see destination info \n3. create destination \n 4. get all destinations")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            #búa til fall sem sækir dest
            pass
        elif command == "2":
            #búa til fall sem sýnir dest info
            pass
        elif command == "3":
            #búa til fall sem býrtil nýtt dest og bætir því inní csv
            pass
        elif command == "4":
            #búa til fall sem sækir öll dest
            pass
        else:
            print("Invalid command")