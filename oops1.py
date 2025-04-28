class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data executed")

    def travel(self, destination):
        print ("started executing travel method manually")
        print (f"Employee is Traveling to {destination}") 

    
# creating an object/instance of the class employee
sam =  employee()

# #print attributes of the object
# print (sam.id)
# sam.travel("New York")
print (type(sam))
