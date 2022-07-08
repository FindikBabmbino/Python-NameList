import sys

namesList = []
while True:
    nameToAdd=input("Insert name to go into the list: ")
    if nameToAdd != "":
        if nameToAdd.isnumeric()==True:
            print("Inserted a number, insert characters please")
            continue
        namesList.append(nameToAdd)
        while True:
            try:
                quit = int(input("Do you want to quit (0/1): "))
            except:
                print("Invalid character")
                continue
            if (quit > 1 or quit < 0):
                print("Insert valid number")
            else:
                break
    if quit == 1:
        break

print("These are the names: ",end="")
for i in namesList:
    if i != namesList[len(namesList)-1]:
        print(i, end=", ")
    else:
        print(i)
        input("Input any key to quit")
        sys.exit()