class Employee:
    emp_id = ""
    name = ""
    surname = ""
    salary = ""
    rec_date = ""
    position = ""
    mark = ""

    def __init__(self, emp_id=None, name=None, surname=None, salary=None, rec_date=None, position=None, mark=None):
        self.emp_id = emp_id if emp_id is not None else ""
        self.name = name if name is not None else ""
        self.surname = surname if surname is not None else ""
        self.salary = salary if salary is not None else ""
        self.rec_date = rec_date if rec_date is not None else ""
        self.position = position if position is not None else ""
        self.mark = mark if mark is not None else ""

    def printEmp(self):
        return self.emp_id + "\t" + self.name + "\t" + self.surname + "\t" + self.salary + "\t" + self.rec_date + "\t" + self.position + "\t" + self.mark
