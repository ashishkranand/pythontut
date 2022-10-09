class Employee:
    no_of_leaves = 8

    def __init__(self,aname , asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return  f"Name is {self.name}. Salary is {self.salary} andn role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good."+string)


class Programmer(Employee):
    no_of_holiday = 56
    def __init__(self,aname , asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"Programmer's name is {self.name}. Salary is {self.salary} andn role is {self.role} . The language is {self.languages}"


ashish = Employee("Ashish",125,"Instructor")
aklesh = Employee("Aklesh",234,"student")
gopal = Programmer("Gopal",435,"Programmer",["c++"])
ram = Programmer("Ram",884,"Programmer",["Python"])
print(ram.printprog())
print(ram.no_of_holiday)



