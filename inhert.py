class Animal():
    def __init__(self, name):
        # Constructor: sets the 'name' attribute when an object is created
        self.name = name

    def speak(self):
        # Instance method: prints a generic animal sound
        print (f"{self.name} makes a sound.")


# Dog inherits from Animal
class Dog(Animal):
    # Define the child class Dog that inherits from Animal
    def speak(self):
        # Overridden method: specific behavior for dogs
        print (f"{self.name} barks.")


# animal = Animal("panda")
# animal.speak()  # Output: panda makes a sound.
dog = Dog("Cat")
dog.speak()  # Output: Cat barks.
          