##getter and setter

from oops_project import chatbook
chatbook.set_id(111)
user1 = chatbook()

print (user1.id)
# user1.get_name
# user1.set_name("John Doe")
# print(user1.get_name())  # Output: John Doe
# user1.set_name(123)  # Raises ValueError: Name must be a string.

user2 = chatbook()
print(user2.id)  