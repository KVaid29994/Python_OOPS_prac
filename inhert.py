class Animal:
    def __init__(self, name):
        # Constructor: sets the 'name' attribute when an Animal object is created
        self.name = "Buddy"

    def speak(self):
        # Instance method: prints a generic animal sound
        print(f"{self.name} makes a sound.")


# 🐶 Dog inherits from Animal
class Dog(Animal):

    def __init__(self, breed):
        # Child class constructor: sets its own attribute and parent's attribute
        super().__init__()  # ✅ Calls parent Animal class constructor to set 'name'
        self.breed = breed  # Child's own attribute

    def speak(self):
        # Overridden method: customized behavior for Dog
        print(f"{self.name} barks. He is a {self.breed}.")


# 🧪 Usage

# Create an Animal object
animal = Animal("Panda")
animal.speak()  
# Output: Panda makes a sound.

# Create a Dog object
dog = Dog("Golden Retriever")
dog.speak()  
