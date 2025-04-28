### Modeling a Car 🚗

# Defining a Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started! 🔥")

    def stop_engine(self):
        print(f"{self.brand} {self.model} engine stopped! 🛑")

# Creating objects (instances) of the Car class
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Toyota", "Corolla", 2020)

# Using the methods
car1.start_engine()
car2.start_engine()
car1.stop_engine()


### What's happening here?

###Class defines the template (Car).

###Objects (car1, car2) are real-world cars.

###Methods like start_engine and stop_engine are behaviors of the car.
