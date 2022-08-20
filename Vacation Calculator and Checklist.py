days = input("How many days?\n")
while True:
    currentclothes = input("Will you wear the same clothes today, tomorrow?\n")
    if currentclothes == "yes":
        NewDays = float(days)
        NewDays -= 1
        break
    elif currentclothes == "no":
        NewDays = float(days)
        break
    else:
        print("Either type yes or no")
shirtspants = float(NewDays) / 2
print("You need " + str(shirtspants) + " shirts, pants and " + str(days) + " pairs of socks ")
checklist = ["vacation bag", "phone charger", "facewash", "pills",  "wallet", "keys", "phone", "hairbrush", str(shirtspants) + " pants", str(shirtspants) + " shirts", , str(days) + " pairs of socks"]
print("On you checklist is\n" + str(checklist))
while True:
    choice = input("Do you want to add anything else? yes or no\n")
    if choice == "yes":
        item_added = input("What do you wanna add?\n")
        checklist.append(item_added)
        print("On you checklist is\n" + str(checklist))
    elif choice == "no":
        print("On you checklist is\n" + str(checklist))
        break
    else:
        print("Either type yes or no")
print("On you checklist is\n" + str(checklist), file=open("checklist.txt", "w"))
while True:
    checklistchoice = input("Do you want to go through your checklist?\n")
    if checklistchoice == "yes":
        for x in checklist:
            while True:
                checklistcheck = input("Do you have " + x + "?\n")
                if checklistcheck == "yes":
                    break
                elif checklistcheck == "no":
                    input("type anything when you are ready to go to next item\n")
                    break
                else:
                    print("Either type yes or no")
    elif checklistchoice == "no":
        print("On you checklist is\n" + str(checklist))
        break
    else:
        print("Either type yes or no")
