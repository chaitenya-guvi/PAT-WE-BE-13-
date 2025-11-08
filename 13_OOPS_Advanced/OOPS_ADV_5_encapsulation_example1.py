class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount < 0:
            print("Invalid salary amount")
        else:
            self.__salary = amount

emp = Employee("John", 50000)
print(emp.get_salary())   # access via getter → 50000

emp.set_salary(60000)     # modifying safely
print(emp.get_salary())   # 60000

emp.set_salary(-10000)    # invalid change
print(emp.get_salary())   # still 60000
