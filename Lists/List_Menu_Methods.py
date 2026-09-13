list = []
choice = 0

while choice != 10:
    print("\n--- |List Operations| ---")
    print("[1].Insert data")
    print("[2].Delete data")
    print("[3].Serach")
    print("[4].Display")
    print("[5].Sort list")
    print("[6].Reverse list")
    print("[7].Count")
    print("[8].Maximum")
    print("[9].Minimum")
    print("[10].Exit")

    choice = int(input("Enter choice (1-10) : "))
    if choice == 1:
        data = int(input("Enter data : "))
        list.append(data)
        print("Element Inserted!")

    elif choice == 2:
        if len(list) == 0:
            print("List is Empty!")
        else:
            value = int(input("Enter an element to delete : "))
            if value in list:
                list.remove(value)
                print("Element deleted!")
            else:
                print("Element not found!")

    elif choice == 3:
        if len(list) == 0:
            print("List is empty!")
        else:
            value = int(input("Enter an element to search : "))
            if value in list:
                list.index(value)
                print(f"Element found : {value}")
            else:
                print("Element not found!")

    elif choice == 4:
        if len(list) == 0:
            print("List is empty!")
        else:
            print(list)

    elif choice == 5:
        if len(list) == 0:
            print("List is empty!")
        else:
            list.sort()
            print(f"Sorted List : {list}")

    elif choice == 6:
        if len(list) == 0:
            print("List is empty!")
        else:
            list.reverse()
            print(f"Reverse List : {list}")

    elif choice == 7:
        count = list.count()
        print(f"Number of data : {count}")

    elif choice == 8:
        if len(list) == 0:
            print("List is empty!")
        else:
            print(f"Maximum element in list : {max(list)}")

    elif choice == 9:
        if len(list) == 0:
            print("List is empty!")
        else:
            print(f"Minimum element in list : {min(list)}")

    elif choice == 10:
        exit = input("Do you want to exit? (y/n) : ")
        if exit == 'y' or exit == 'Y':
            print("Program Exited Sucessfully!")
            break
        else:
            choice == 0

    else:
        print("Invalid Choice!")
