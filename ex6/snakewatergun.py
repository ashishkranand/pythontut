import random
game =["s","w","g",]
choice = random.choice(game)
print("WELCOME TO SNAKE , WATER , GUN GAME 🙏")
count=0
countc=0
num=1
while(num<=10):
    inp = input("Enter your choice (choices are s for snake , w for water , g for gun) :--> ")
    if (choice == "s" and inp == "g"):
        print("You won")
        count += 1
    elif (choice == "g" and inp=="s"):
        print("Computer won")
        countc += 1
    elif (choice == "s" and inp == "w"):
        print("You won")
        count += 1
    elif (choice == "w" and inp == "s"):
        print("Computer won")
        countc += 1
    elif (choice == "w" and inp == "g"):
        print("You won")
        count += 1
    elif (choice == "g" and inp == "w"):
        print("Computer won")
        countc += 1
    elif(choice=="g" and inp=="g"):
        print("game die")
    elif (choice == "w" and inp == "w"):
        print("game die")
    elif (choice == "s" and inp == "s"):
        print("game die")
    else:
        print("Wrong choice entered")
    num+=1

if(count>countc):
    total=count-countc
    print(f"You won by {total} points ",)
elif(count==countc):
    print("GAME TIE OR ERROR OCCURED DUE TO WRONG OPTION SELECTED")
else:
    total = countc - count
    print(f"Computer won by {total} points ", )
