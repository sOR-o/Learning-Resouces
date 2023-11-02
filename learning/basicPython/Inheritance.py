# Parent class
class Animal:
    """This class represents an animal."""

    def __init__(self, name):
        """Constructor to initialize the name attribute."""
        self.name = name

    def speak(self):
        """Method to make the animal speak."""
        pass

# Child class
class Dog(Animal):
    """This class represents a dog."""

    def speak(self):
        """Method to make the dog bark."""
        print("Woof!")

# Creating objects
dog = Dog("Buddy")
dog.speak()
