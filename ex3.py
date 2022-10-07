# Pattern Printing
num = int(input("Enter any number:->"))
check = bool(int(input("Enter either 0 or 1 :->")))
if check==True:
    for i in range(0, num):
        for j in range(0, i + 1):
            print("*", end=' ')
        print(" ")
elif check == False:
    for i in range(num, 0, -1):
        for j in range(0, i ):
            print("*", end=' ')
        print(" ")