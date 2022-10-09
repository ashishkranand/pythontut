class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return  f"Name is {self.name}. Salary is {self.salary} andn role is {self.role}"

ashish = Employee()
aklesh = Employee()

ashish.name= "Ashish"
ashish.salary = 1234
ashish.role = "Instructor"
aklesh.name = "Aklesh"
aklesh.salary = 345654
aklesh.role = "student"

print(ashish.printdetails())