class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

Employee('Clément', '18', '2300').display_details()