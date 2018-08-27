from Models.Employee import Employee
from Utilities.FileOperation import FileOperation

class Company:
    list = None
    
    def __init__(self, empList = []):
        self.list = empList if empList is not None else []

    #not working yet
    def removeEmployee(self, id):
        del list[id]

    def viewList(self):
        print("[emp_id]\t[name]\t[surname]\t[salary]\t[rec_date]\t[position]\t[mark]")

        emp = Employee()
        for emp in self.list:
            print(emp.printEmp())

    def add_employee(self):
        add_menu = [" ", "Provide employee info:", "name", "surname", "salary", "rec_date", "position", "mark"]

        for e in add_menu:
            print(e)

        tmpEmp = Employee()

        tmpEmp.emp_id = "1"
        tmpEmp.name = input()
        tmpEmp.surname = input()
        tmpEmp.salary = input()
        tmpEmp.rec_date = input()
        tmpEmp.position = input()
        tmpEmp.mark = input()

        self.list.append(tmpEmp)

    def sub(self):
        return "sub"

    def no_option(self):
        return "No such option!"

    def import_employees_list(self):
        list = FileOperation.readEmployees()
        return list

    def export_employees_list(self, empList):
        return FileOperation.writeEmployees(empList)

    def quit(self):
        return "Exiting..."

    def pandasR(self):
        return FileOperation.pandasRead()

    def do_operation(self, switch):
        handler = {
        '1': self.add_employee,
        '2': self.sub,
        '3': self.viewList,
        '4': self.import_employees_list,
        '5': self.export_employees_list,
        'q': self.quit
        }
        return handler.get(switch, self.no_option)()