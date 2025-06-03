import random

real_user = "John"
bot_user = "Jack"


while True:
    try:
        pencils = int(input("How many pencils would you like to use: "))
        if pencils == 0:
            print("The number of pencils should be positive")
        elif pencils < 0:
            print("The number of pencils should be numeric")
        else:
            break
    except ValueError:
        print("The number of pencils should be numeric")
first =  input("Who will be the first (John, Jack): ")
while first != real_user and first != bot_user:
    print("Choose between John and Jack")
    first =  input("Who will be the first (John, Jack): ")


while pencils > 0:
    print("|" * pencils)
    print(f"{first}'s turn:")
    if first == real_user:
        while True:
            remove_pencils = input()
            if remove_pencils not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            else:
                if int(remove_pencils) > pencils:
                    print("Too many pencils were taken")
                else:
                    pencils -= int(remove_pencils)
                    break
    else:
        if pencils % 4 == 1:
            bot_remove = random.randint(1, min(3, pencils))
        elif pencils % 4 == 0:
            bot_remove = 3
        elif pencils % 4 == 3:
            bot_remove = 2
        else:
            bot_remove = 1
        print(bot_remove)
        pencils -= bot_remove


    if pencils == 0:
        winner = bot_user if first == real_user else real_user
        print(f"{winner} won!")
        break


    first = bot_user if first == real_user else real_user




