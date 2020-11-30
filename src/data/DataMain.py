import csv
import os


class DataMain:
    def __init__(self):
        print("inside data")
    
    def get_employees(self):
        print(os.getcwd())
        emploee_list = []
        with open("data\emploee.csv", newline='',encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                emploee_list.append(line)
            return emploee_list
