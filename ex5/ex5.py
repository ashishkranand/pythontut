print("HEALTH MANAGEMENT SYSTEM")
print("\n")
def getdate():
    import datetime
    return datetime.datetime.now()

def getname():
    name = input("Enter name (Ashish , Aklesh , Prabhkar) :--> ")
    return name

name= getname()
if(name=="Ashish"):
    print("Welcome to the health management system of Ashish")
    print("Enter 1 for diet and 2 for excercise.")
    ch=int(input("Enter your choice from the above list:--> "))
    if(ch==1):
        print("Welcome to diet management system of Ashish.")
        print("For writing data in file press 1 or for reading press 2")
        num=int(input("What do you want to do enter number according to above choices:--> "))
        if(num==1):
            diet=input("What do you want to enter in diet of Ashish:--> ")
            with open("ashish_diet.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(diet)
                f.write("\n")
        elif(num==2):
            content = open("ashish_diet.txt")
            f = content.read()
            print(f)
    elif(ch==2):
        print("Welcome to excercise management system of Ashish.")
        print("For writing data in file press 1 or for reading press 2")
        num = int(input("What do you want to do enter number according to above choices:--> "))
        if (num == 1):
            ex = input("What do you want to enter in excercise of Ashish:--> ")
            with open("ashish_ex.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(ex)
                f.write("\n")
        elif (num == 2):
            content = open("ashish_ex.txt")
            f = content.read()
            print(f)
    else:
        print("wrong choice selected")
elif(name=="Aklesh"):
    print("Welcome to the health management system of Aklesh")
    print("Enter 1 for diet and 2 for excercise:-->")
    ch = int(input("Enter your choice from the above list:--> "))
    if (ch == 1):
        print("Welcome to diet management system of Aklesh.")
        print("For writing data in file press 1 or for reading press 2")
        num = int(input("What do you want to do enter number according to above choices:--> "))
        if (num == 1):
            diet = input("What do you want to enter in diet of Aklesh:--> ")
            with open("aklesh_diet.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(diet)
                f.write("\n")
        elif (num == 2):
            content = open("aklesh_diet.txt")
            f = content.read()
            print(f)
    elif (ch == 2):
        print("Welcome to excercise management system of Aklesh.")
        print("For writing data in file press 1 or for reading press 2")
        num = int(input("What do you want to do enter number according to above choices:--> "))
        if (num == 1):
            ex = input("What do you want to enter in excercise of Aklesh:--> ")
            with open("aklesh_ex.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(ex)
                f.write("\n")
        elif (num == 2):
            content = open("aklesh_ex.txt")
            f = content.read()
            print(f)
    else:
        print("wrong choice selected")
elif(name=="Prabhakar"):
    print("Welcome to the health management system of Prabhakar")
    print("Enter 1 for diet and 2 for excercise:-->")
    ch = int(input("Enter your choice from the above list:--> "))
    if (ch == 1):
        print("Welcome to diet management system of Prabhakar.")
        print("For writing data in file press 1 or for reading press 2")
        num = int(input("What do you want to do enter number according to above choices:--> "))
        if (num == 1):
            diet = input("What do you want to enter in diet of Prabhakar:--> ")
            with open("prabhakar_diet.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(diet)
                f.write("\n")
        elif (num==2):
            content = open("prabhakar_diet.txt")
            f = content.read()
            print(f)
    elif (ch == 2):
        print("Welcome to excercise management system of Prabhakar.")
        print("For writing data in file press 1 or for reading press 2")
        num = int(input("What do you want to do enter number according to above choices:--> "))
        if (num == 1):
            ex = input("What do you want to enter in excercise of Prabhakar:--> ")
            with open("prabhakar_ex.txt", "a") as f:
                time = getdate()
                f.write(str(time))
                f.write(" ")
                f.write(ex)
                f.write("\n")
        elif (num == 2):
            content = open("prabhakar_ex.txt")
            f = content.read()
            print(f)
    else:
        print("wrong choice selected")
else:
    print("Error!!! , You have to enter only from list given above...")
