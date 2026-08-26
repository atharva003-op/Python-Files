num = []
choice = 0

while choice != 6:
    print("\n--- |List Operations| ---")
    print("[1].Insert")
    print("[2].Delete")
    print("[3].Display")
    print("[4].Search")
    print("[5].Update")
    print("[6].Exit")
    choice = int(input("Enter choice : "))

    if choice == 1:
        num.append(int(input("Enter an element to insert : ")))
        print("Element Inserted!")

    elif choice == 2:
        if len(num) == 0:
            print("List is empty!\n")
        else:
            value = int(input("Enter an element to delete : "))
            if value in num:
                num.remove(value)
                print("Element Deleted!")
            else:
                print("Element not found!")

    elif choice == 3:
        if len(num) == 0:
            print("List is empty!\n")
        else: 
            print(f"List : {num}")

    elif choice == 4:
        if len(num) == 0:
            print("List is empty!\n")
        else:
            find = int(input("Enter a number to find : "))
            if find in num:
                print("Element found!")
                print(f"Element : {find}")    
            else:
                print("Element not found!")

    elif choice == 5:
        if len(num) == 0:
            print("List is empty!\n")
        else:
            update = int(input("Enter an element to update : "))

            if update in num:
                new_value = int(input("Enter new value : "))

                index = num.index(update)
                num[index] = new_value

                print("Element updated!")
            else:
                print("Element not found!")

    elif choice == 6:
        print("Program Exited Sucessfully!")

    else : print("Invalid choice!\n")
