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

for emp in [FullTimeEmployee(), PartTimeEmployee(), Freelancer()]:
    show_salary(emp)
