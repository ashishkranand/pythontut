class Employee:
    no_of_leaves = 8
    var =8

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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"Name is {self.name} and Salary is {self.game}"

class Coolprogrammer(Employee,Player):
    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

ashish = Employee("Ashish",125,"Instructor")
aklesh = Employee("Aklesh",234,"student")

subhash = Player("Subhash","cricket")
ram = Coolprogrammer("Ram","54345","CoolProg")
# det = ram.printdetails()
# ram.printlanguage()
# print(det)
print(Coolprogrammer.var)






