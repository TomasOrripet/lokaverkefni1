from logic.LogicMain import LogicMain

class Vehicles:
    def __init__(self):
        self.logic = LogicMain()

    def vehicle_options(self):
        print("1. see all vehicles info \n2. Create Vehicle \n3. see vehicle info \n4. see all vehicle condition \n5. see all vehicle condition status \n6. change vehicle condition status")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            resault = self.logic.get_all_Vehicles()
            for line in resault:
                print(line)
        elif command == "2":
            resault = self.logic.create_vehicle()
            return
        elif command == "3":
            vehicle_id = input("Input vehicle ID: ")
            resault = self.logic.get_vehicle(vehicle_id)
            print(resault)
        elif command == "4":
            resault = self.logic.get_vehicle_condition()
            print(resault)
        elif command == "5":
            resault = self.logic.get_vehicle_condition_status()
        elif command == "6":
            resault = self.logic.change.vehicle_condition_status()    
        else:
            print("Invalid command")
        


