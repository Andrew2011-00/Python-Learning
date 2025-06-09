import random

dic_guests = {}
print("Enter the number of friends joining (including you):")
guests = int(input())
if guests <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(guests):
        dic_guests[input().capitalize()] = 0
    print("Enter the total bill value:")
    bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    yes_no = input().lower()
    if yes_no == "yes":
        random_guest = random.choice(list(dic_guests.keys()))
        print(f"{random_guest} is the lucky one!")
        for n in dic_guests:
            if n != random_guest:
                dic_guests[n] = round(bill / (guests - 1), 2)


        print(dic_guests)

    else:
        print("No one is going to be lucky")
        for t in dic_guests:
            dic_guests[t] = round(bill / guests, 2)
        print(dic_guests)



