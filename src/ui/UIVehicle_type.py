from logic.LogicMain import LogicMain

class Vehicle_type:
    def __init__(self):
        self.logic = LogicMain()

    def vehicle_type_options(self):
          print("1. get vehicle type info \n2. see vehicle type info \n3. get vehicle rate \n 4. create vehicle")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            #búa til fall sem sækir veh_type info
            pass
        elif command == "2":
            #búa til fall sem sýnir veh_type info
            pass
        elif command == "3":
            #búa til fall sem sækir veh_type rate
            pass
        elif command == "4":
            #búa til fall sem býr til vehcle og bætir við csv
            pass
        else:
            print("Invalid command")