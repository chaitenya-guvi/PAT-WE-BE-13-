class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)    # calls Employee's __init__
        self.language = language



dev1 = Developer("Alice", "Python")
print(dev1.name)
print(dev1.language)


dev2 = Developer("Bob", "JavaScript")
print(dev2.name)
print(dev2.language)


