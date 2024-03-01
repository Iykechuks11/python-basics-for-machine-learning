# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# class Dog:
#     pass

# obj = Dog()

class Dog:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"My name is {self.name}")
# Driver code 
# Object instantiation
Rodger = Dog("Rodger")

# Accessing class attributes
# print(f"The name of my dog is {Rodger.name}")
print(f"{Rodger.name} is a {Rodger.__class__.attr1}")
Rodger.speak()