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
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        #Line 18 and 19 ke badle 21 line
        return cls(*string.split("-"))

ashish = Employee("Ashish",125,"Instructor")
aklesh = Employee("Aklesh",234,"student")
ram = Employee.from_dash("karan-454-student")
print(ram.no_of_leaves)

ashish.change_leaves(34)
print(ashish.no_of_leaves)