    
    
print("Welcome to Python CLI Calculator!\n")

num1 = float(input("What is the first number? : "))

while True:

    operations = input("+\n-\nx\n/\nPick an operation: ")

    if operations not in ["+", "-", "x", "/"]:
        print("Invalid operation. Try again.")
        continue

    num2 = float(input("What is the second number? : "))

    if operations == "+":
        result = num1 + num2

    elif operations == "-":
        result = num1 - num2

    elif operations == "x":
        result = num1 * num2

    elif operations == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue

        result = num1 / num2

    print(f"{num1} {operations} {num2} = {result}")

    choice = input(
        f"\nType 'y' to continue with {result}, "
        " 'n' to start a new calculation, "
        "or 'q' to quit: "
    ).lower()

    if choice == "y":
        num1 = result

    elif choice == "n":
        num1 = float(input("What is the first number? : "))

    elif choice == "q":
        print("Thank you for using my CLI calculator!")
        break
    
    
    
    
    
    
    
    
    
    
    
            

    
    