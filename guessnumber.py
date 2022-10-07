n=25
numofgues=1
print("You get only 9 chances:-")
while(numofgues<=9):
    guesnum=int(input("Enter any number for guess:->"))
    if guesnum<25:
        print("You have entered lesser number.")
    elif guesnum>25:
        print("You hava entered greater number.")
    else:
        print("You won\n")
        print("You took ",numofgues,"for guessing")
        break
    print(9-numofgues,"chances left")
    numofgues=numofgues+1
    if(numofgues>9):
        print("Game over , You have reached maximum number of chances")