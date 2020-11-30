from logic.LogicMain import LogicMain

class Customer:
    def __init__(self):
        self.logic = LogicMain()

    def customer_options(self):
        print("1. Get all Customers info \n2. Get Customer info")
        command = input("Input your command: ")
        command = command.lower()
        if command == "1":
            resault = self.logic.all_customers()
            for line in resault:
                print(line)
        elif command == "2":
            customer_id = input("Input customer ID: ")
            resault = self.logic.get_customer(customer_id)
            return
        else:
            print("Invalid command")
