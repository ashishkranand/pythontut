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

ashish = Employee("Ashish",125,"Instructor")
aklesh = Employee("Aklesh",234,"student")

ashish.change_leaves(34)
print(ashish.no_of_leaves)