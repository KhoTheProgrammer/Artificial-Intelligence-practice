from person import Person
import sys
class Student(Person):
    def __init__(self, fname, lname, year):
        self.firstname = fname
        self.lastname = lname
        self.graduataiony_year = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduataiony_year,
        )

    def __str__(self):
        return f"Firstname: {self.firstname}\nLastname: {self.lastname}\nGraduation Year: {self.graduataiony_year}"


def main():
    y = Student("khoo", "Pad", 2027)
    y.welcome()
    print(y)
    sys.exit(-1)
    
main()

