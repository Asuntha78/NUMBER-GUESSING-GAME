print ("Hello there!")
print("I am thinking of a number between 0 and 10")
print("You have 3 chances, let's see if you can guess it :)")
chance = 0
won = False
#guessed number is 8
while chance < 3:
    number = int(input("Number?"))
    if number == 8 :
        print("Correct guess!")
        print("You won!!!")
        won = True
        break
    else:
        print("Try again!")
    chance += 1
# Only print when all 3 chances are over and still not won
if not won:
    print("Three chances are over, try again later!")
    