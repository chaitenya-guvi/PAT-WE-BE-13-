"""Encapsulation provides:

Data protection — internal details are hidden.

Controlled access — data can only be changed safely.

Cleaner design — users interact through methods, not internal variables."""

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.__engine_status = "OFF"

    def start_engine(self):
        self.__engine_status = "ON"
        print(f"{self.brand} engine started")

    def stop_engine(self):
        self.__engine_status = "OFF"
        print(f"{self.brand} engine stopped")

    def get_engine_status(self):
        return self.__engine_status

car = Car("Tesla")
print(car.get_engine_status())  # OFF
car.start_engine()              # Tesla engine started
print(car.get_engine_status())  # ON
car.__engine_status = "BROKEN"   # external change ignored
print(car.get_engine_status())  # still
