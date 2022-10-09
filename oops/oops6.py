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



ashish = Employee("Ashish",125,"Instructor")
aklesh = Employee("Aklesh",234,"student")
ram = Employee.from_dash("karan-454-student")
print(ram.printgood("Ashish"))