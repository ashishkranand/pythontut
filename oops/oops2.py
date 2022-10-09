class Employee:
    no_of_leaves = 8
    pass
ashish = Employee()
aklesh = Employee()

ashish.name= "Ashish"
ashish.salary = 1234
ashish.role = "Instructor"
aklesh.name = "Aklesh"
aklesh.salary = 345654
aklesh.role = "student"

print(ashish.no_of_leaves)

print(ashish.__dict__)

ashish.no_of_leaves= 9
print(ashish.no_of_leaves)

