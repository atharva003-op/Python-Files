list = []

add = input("Enter an element to insert : ")
list.append(add)

while True:
    exit = input("Do you want to exit? (y/n) : ")
    if exit == 'y' or exit == 'Y':
        print("Program Exited Sucessfully!")
        break
    else:
        add = input("Enter an element to insert : ")
        list.append(add)

print(list)
