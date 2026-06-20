"""
OOP example in Python.

Topics covered:
- Class
- Object
- Constructor
- self
- Inheritance
- super()
- Method overriding

A SuperCar class inherits from the Car class and adds
extra functionality while reusing the parent class logic.
"""


class Car:
    """Represents a generic car."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_car(self):
        print(f"{self.brand}: is started")

    def show_info(self):
        print(f"Brand: {self.brand} | Model: {self.model}", end=" ")


class SuperCar(Car):
    """A car with additional performance features."""

    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def turbo(self):
        print("Turbo is active")

    def show_info(self):
        super().show_info()
        print(f"| Max speed: {self.max_speed}")
        
        
# Create a SuperCar object and test its methods
example_car = SuperCar("BMW", "i8", 240)

example_car.start_car()
example_car.turbo()
example_car.show_info()
