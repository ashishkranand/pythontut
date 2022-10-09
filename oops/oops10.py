class Employee:
    no_of_leaves = 8
    var =8
    _protec=2
    __private = 98

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

emp = Employee("Ashish",78,"jkh")
print(emp._Employee__private)



