class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("im in the constructor")

    def __str__(self):
        return f"{self.firstname}{self.lastname}"

    def printname(self):
        print(f"Hello my name is {self.firstname} {self.lastname}")

    def myfunc(self):
        print(f"Hello my name is {self.firstname} {self.lastname}")
