#from logic.LogicMain import LogicMain held þetta þarf ekki
from ui.UIEmploee import Emploees
from ui.UICustomer import Customer
from ui.UIVehicle_type import Vehicle_type
from ui.UIVehicles import Vehicles
from ui.UIDestinations import Destinations
from ui.UIContracts import Contracts
from ui.UIReports import Reports




class UIMain:
    def __init__(self):
        print("inside ui")
        #self.logic = LogicMain() þarf örgl ekki hér
        self.ui_emploee = Emploees()
        self.ui_customer = Customer()
        self.ui_vehicle_type = Vehicle_type()
        self.ui_vehicles = Vehicles()
        self.ui_destination = Destinations()
        self.ui_contracts = Contracts()
        self.ui_reports = Reports()

        self.ui_loop()

    def ui_loop(self):
        while True:
            print("What are you looking for?")
            print("1. Employees \n2. Customer \n3. Vehicle type \n4. Vehicles \n5. Destinations \n6. Contracts \n7. Reports")
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                self.ui_emploee.emploee_options()
            elif command == "2":
                self.ui_customer.customer_options()
                pass
            elif command == "3":
                self.ui_vehicle_type.vehicle_type_options()
                pass
            elif command == "4":
                self.ui_vehicles.vehicle_options()
            elif command == "5":
                self.ui_destination.destination_options()
                pass
            elif command == "6":
                self.ui_contracts.contract_options()
                pass
            elif command == "7":
                self.ui_reports.report_options()
                pass
            elif command == "q":
                break
            else:
                print("Invalid command")

