class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def status(self):
        result = f'{self.name} has been employed'
        return result


class Employee(Person):

    def __init__(self, name, age):
        Person.__init__(self, name, age)

a = Employee('John', 28)
print(a.status())