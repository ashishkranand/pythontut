import random
game =["snake","water","gun",]
choice = random.choice(game)
print("WELCOME TO SNAKE , WATER , GUN GAME 🙏")
count=0
countc=0
num=1
while(num<=10):
    inp = input("Enter your choice (choices are snake , water , gun) :--> ")
    if (choice == "snake" and inp == "gun"):
        print("You won")
        count += 1
    elif (choice == "gun" and inp=="snake"):
        print("Computer won")
        countc += 1
    elif (choice == "snake" and inp == "water"):
        print("You won")
        count += 1
    elif (choice == "water" and inp == "snake"):
        print("Computer won")
        countc += 1
    elif (choice == "water" and inp == "gun"):
        print("You won")
        count += 1
    elif (choice == "gun" and inp == "water"):
        print("Computer won")
        countc += 1
    elif(choice=="gun" and inp=="gun"):
        print("game die")
    elif (choice == "water" and inp == "water"):
        print("game die")
    elif (choice == "snake" and inp == "snake"):
        print("game die")
    else:
        print("Wrong choice entered")
    num+=1

if(count>countc):
    total=count-countc
    print(f"You won by {total} points ",)
else:
    total = countc - count
    print(f"Computer won by {total} points ", )
