import os
import globals
from Models.Employee import Employee
from Models.Company import Company
from Utilities.FileOperation import FileOperation

#----------------------------------------------------------------------            
if __name__ == "__main__":
    
    c = Company()

    var = ""
    while var not in ("q", "quit"):
        #os.system('cls')

        for e in globals.main_menu:
            print(e)
    
        var = input()
        print(c.do_operation(var))

    

