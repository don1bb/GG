class Human:
    def __init__(self, name):
        self.name = name
class Person:
    def __init__(self, age):
         self.age = age
class One(Human):
    def sss(self):
        print('Машина едет')
class Two(Person):
    def sss(self):
        print('Машина не едет')

class Three(One,Two):
    def __init__(self, name, age):
        One.__init__(self, name)
        Two.__init__(self, age)

    def __str__(self):
        return f' {self.name} {self.age}'

h=Three('Adam',50)
print(h)
