class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("im in the constructor")
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello my name is " + self.name + " and i am " + str(self.age) + " years old")

p1 = Person("khoo", 56)
print(p1)

        