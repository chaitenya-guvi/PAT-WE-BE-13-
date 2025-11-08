from functools import partial


class Employee:
    def calculate_salary(self):
        raise NotImplementedError("Subclass must implement this method")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000

class Freelancer(Employee):
    def calculate_salary(self):
        return 15000

def show_salary(employee):
    print(f"Salary: {employee.calculate_salary()}")

fulltimeemp = FullTimeEmployee()
partimeemp = PartTimeEmployee()
freelanceremp = Freelancer()

list1 = [fulltimeemp, partimeemp, freelanceremp]

for emp in list1:
    show_salary(emp)
