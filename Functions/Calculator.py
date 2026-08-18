def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def square(a):
    return a * a

def get_numbers():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    return a, b

choice = 0

while choice != 6:
    print("\n--- |Calculator| ---")
    print("[1].Addition")
    print("[2].Substraction")
    print("[3].Multiplication")
    print("[4].Division")
    print("[5].Sqaure")
    print("[6].Exit")
    choice = int(input("Enter choice (1-6) :  "))

    if choice == 1:
        a , b = get_numbers()
        print(f"The addition of {a} and {b} is : {add(a,b)}")

    elif choice == 2:
        a , b = get_numbers()
        print(f"The substraction of {a} and {b} is : {subtract(a,b)}")

    elif choice == 3:
        a , b = get_numbers()
        print(f"The Multiplication of {a} and {b} is : {multiply(a,b)}")

    elif choice == 4:
        a , b = get_numbers()
        if (b > 0):
            print(f"The division of {a} and {b} is : {divide(a,b)}")
        else:
            print("Cannot divide by zero!")

    elif choice == 5:
        a = int(input("Enter number to get square : "))
        print(f"The square of {a} : {square(a)}")

    elif choice == 6:
        print("Program Exited Sucessfully!")

    else:
        print("Invaild choice!")
