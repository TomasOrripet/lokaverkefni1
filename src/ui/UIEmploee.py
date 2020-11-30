from logic.LogicMain import LogicMain

class Emploees:
    def __init__(self):
        self.logic = LogicMain()

    def emploee_options(self):
        print("1. Get all Employees info \n2. Create employee \n3. Get employee info \n4. Change Employee")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            resault = self.logic.all_employees()
            for line in resault:
                print(line)
        elif command == "2":
            resault = self.logic.create_employee()
            return
        elif command == "3":
            employee_id = input("Input employee ID: ")
            resault = self.logic.get_employee(employee_id)
            print(resault)
        elif command == "4":
            employee_id = input("Input employee ID: ")
            resault = self.logic.change_employees(employee_id)
            print(resault)
        else:
            print("Invalid command")    