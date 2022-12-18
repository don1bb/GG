class Калькулятор:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __truediv__(self, other):
        return self.val / other.val

a = Калькулятор(int(input('число =')))
s = Калькулятор(int(input('число =')))
print(a + s)
print(a - s)
print(a * s)
print(a / s)


