# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 7 Assignment 4

class NumCouple:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def minimum(self):
        if (self.num1 <= self.num2):
            return self.num1
        else:
            return self.num2

    def maximum(self):
        if (self.num1 <= self.num2):
            return self.num2
        else:
            return self.num1

    def product(self):
        return self.num1*self.num2

class NumThruple(NumCouple):
    def __init__(self, num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3

    def minimum(self):
        super_min = super().minimum()
        if (super_min <= self.num3):
            return super_min
        else:
            return self.num3

    def maximum(self):
        super_max = super().maximum()
        if (super_max <= self.num3):
            return self.num3
        else:
            return super_max

    def product(self):
        return super().product() * self.num3


# hard-coded lines
couple = NumCouple(4, 7)
print(f"The couples minimum is {couple.minimum()}")
print(f"The couples maximum is {couple.maximum()}")
print(f"The couples product is {couple.product()}")
thruple = NumThruple(3, 5, 2)
print(f"The thruples minimum is {thruple.minimum()}")
print(f"The thruples maximum is {thruple.maximum()}")
print(f"The thruples product is {thruple.product()}")