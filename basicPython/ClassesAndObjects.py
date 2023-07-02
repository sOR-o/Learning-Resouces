# Class definition
class Car:
    """This class represents a car object."""

    def __init__(self, brand, model):
        """Constructor to initialize brand and model attributes."""
        self.brand = brand
        self.model = model

    def drive(self):
        """Method to simulate driving the car."""
        print("Driving", self.brand, self.model)

# Creating objects
car1 = Car("Toyota", "Camry")
car1.drive()
