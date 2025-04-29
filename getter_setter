'''Why Use Getters and Setters?
Encapsulation (protects data)

Validation before setting

Debugging and logging control

Read-only properties if needed (only getter)
'''

class Student:
    def __init__(self, name):
        self.__name = name
    
    @property
    ### @property turns a method into a getter for a read-only attribute.
    ### You can access the method like a normal attribute without using parentheses ().
    ### This is useful for attributes that should not be modified directly.'''


    def name(self):
        return self.__name
    
    @name.setter
    ##@name.setter allows setting (modifying) the value of the property.
    ### It is used to define a setter method for the property.
    ##It binds a method to run when you assign a value.


    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string.")

s = Student("John")
print(s.name)   # ✅ John (getter)
s.name = "Doe"  # ✅ Doe (setter)
print(s.name)
