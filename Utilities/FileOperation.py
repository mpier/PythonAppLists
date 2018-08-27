import csv
import globals
import pandas
from Models.Employee import Employee

class FileOperation(object):
    field_names = ['emp_id', 'name', 'surname', 'salary', 'rec_date', 'position', 'mark']

    @staticmethod
    def readEmployees():
        emp_list = []
        with open(globals.file_path, mode='r', encoding='utf-8', errors='ignore') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(f'row["emp_id"]', f'row["name"]', f'row["surname"]', f'row["salary"]', f'row["rec_date"]', f'row["position"]', f'row["mark"]')
                emp_list.append(emp)
                print(emp_list.count)
        return emp_list

    @staticmethod
    def writeEmployees(emp_list):
        with open(globals.file_path, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            
            emp = Employee
            for emp in emp_list:
                writer.writerow({'emp_id': emp.emp_id, 'name': emp.name, 'surname': emp.surname, 'salary': emp.rec_date, 'position': emp.position, 'mark': emp.mark})
        return True

    @staticmethod
    def pandasRead():
        df = pandas.read_csv(globals.file_path)
        print(df)
        return 1


