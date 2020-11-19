# Name: Jamar Hill
# Date: 11/18/20
# Description: Assignment 8.c

"""Write a class Employee that has a private data member for an employee's name, ID_number, salary, and email_address"""
class Employee:  # this is the employee class
    def __init__(self,emp_names, emp_ids, emp_sals, emp_emails):  # init method takes four values and uses them to initialize the data members
        self.emp_names = emp_names
        self.emp_ids = emp_ids
        self.emp_sals = emp_sals
        self.emp_emails = emp_emails

    def get_name(self):   # Defines a function to retrieve employee name data
        return self.emp_names

    def get_ID_number(self): # Defines a function to retrieve employee ID data
        return self.emp_ids

    def get_salary(self): # Defines a function to retrieve employee salary data
        return self.emp_sals

    def get_email_address(self): # Defines a function to retrieve employee email address data
        return self.emp_emails


def make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails):  # make_employee_dict takes as a parameter a list of names, ID numbers, salaries, and emails.
    result = {} # adds values to a dictionary
    for x in range(len(emp_names)):  # Creates Employee object where the dictionary key as emp_ids
        emp = Employee(emp_names[x], emp_ids[x], emp_sals[x], emp_emails[x])
        result[emp_ids[x]] = emp
    return result


#Test code with example provided
emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
for x in result:
    #Test for emp_ids "100"
    print(result["100"].get_name())


    #Test for additional data members
    print(result.get(x).get_name(),result.get(x).get_ID_number(),result.get(x).get_salary(),result.get(x).get_email_address())



