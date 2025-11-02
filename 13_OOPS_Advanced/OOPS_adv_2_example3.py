class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def show_address(self):
        print(f"Street: {self.street}, City: {self.city}, Zip: {self.zipcode}")


# derived class

class HomeAddress(Address):
    def __init__(self, street, city, zipcode, house_type):
        # call parent (Address) constructor
        super().__init__(street, city, zipcode)
        self.house_type = house_type

    def show_address(self):
        super().show_address()
        print(f"House Type: {self.house_type}")


class MailingAddress(Address):
    def __init__(self, street, city, zipcode, is_office):
        super().__init__(street, city, zipcode)
        self.is_office = is_office

    def show_address(self):
        super().show_address()
        if self.is_office is True:
            print("Mailing Address: Office")
        else:
            print("Mailing Address: Home")


class Employee:
    def __init__(self, name, home_address, mailing_address):
        self.name = name
        self.home_address = home_address
        self.mailing_address = mailing_address

    def show_info(self):
        print(f"Employee Name: {self.name}")
        print("\nHome Address:")
        self.home_address.show_address()
        print("\nMailing Address:")
        self.mailing_address.show_address()


home = HomeAddress("123 Park St", "Mumbai", "400001", "Apartment")
mailing = MailingAddress("45 MG Road", "Pune", "411001", True)

emp = Employee("Chaitenya", home, mailing)
emp.show_info()
