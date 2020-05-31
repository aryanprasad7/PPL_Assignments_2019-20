guess = 67
print("You will be given 5 chances to guess the number, the number is between 0 to 100")
chance = 5
while(chance):
    usrguess = int(input("Enter your guessed number: "))
    if usrguess < guess:
        print("The number you have guessed is smaller than the number to be guessed")
    elif usrguess > guess:
        print("The number you have guessed is greater than the number to be guessed")
    else:
        print("Hurray!!! YOu guessed the right number")
        break
    chance = chance - 1
if(chance == 0):
    print("OOps!, It seems you are out of chances, try again next time")
# else:
#     print("You were left with ", chance, " chances")
