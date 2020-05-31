import random
print("To begin the dice game, enter 1 as input, any other number to quit")
i = int(input("Enter the number: "))
if i == 1:
    while(1):
        print(random.randint(1, 6))
        con = int(input("Enter 1 to continue, any other number to quit: "))
        if con == 1:
            pass
        else:
            break
