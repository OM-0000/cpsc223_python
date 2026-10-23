#Classes (10/20/26)

class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.weight = 10
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 10
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def bark(self):
        print(f"{self.name} says \"Woof!\"")
    def junk_test():
        print(f"This is a test.")

#So this is how you do inheritance in python
class Bulldog(Dog):
    def __init__(self):
        super().__init__()
    def __init__(self, name, age):
        super().__init__(name, age)

    def sit(self):
        print(f"{self.name} sits.")
    

# Parameter of self in class member functions indicate whether the function is an instance function (so to speak) and a static method
# Static method does not have self as parameter. Call from the class itself.
# The other kind does. Call from an instance.

fido = Dog("Fido", 37)
fluffy = Dog("Fluffy", 13)
print(fido.name)
print(fido.age)
print(fido)
fido.bark()
Dog.junk_test() #this is how you call a static function

fido.weight = 50

print(f"{fido.name} weighs {fido.weight}")

fido = Bulldog("fido", 37)
fido.bark()
fido.sit()