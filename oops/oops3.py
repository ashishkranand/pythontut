class Employee:
    no_of_leaves = 8

    def __init__(self,aname , asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return  f"Name is {self.name}. Salary is {self.salary} andn role is {self.role}"

ashish = Employee("Ashish",125,"Instructor")
# aklesh = Employee()

# ashish.name= "Ashish"
# ashish.salary = 1234
# ashish.role = "Instructor"
# aklesh.name = "Aklesh"
# aklesh.salary = 345654
# aklesh.role = "student"

print(ashish.printdetails())