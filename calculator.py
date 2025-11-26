#taking two numbers and performing action according to user wishes
print("Welcome to the simple calculator!\n")
choice2 = "yes"
while choice2 in ["yes" , "1"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")    
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    choice = input("\nEnter choice (1/2/3/4/5/6): ")
    if choice == '1':
        print(f"\n{n1} + {n2} = {n1 + n2}")
    elif choice == '2':
        print(f"\n{n1} - {n2} = {n1 - n2}")
    elif choice == '3':
        print(f"\n{n1} * {n2} = {n1 * n2}")
    elif choice == '4':
        if n2 != 0:
            print(f"\n{n1} / {n2} = {n1 / n2}")
        else:
            print("\nError: Division by zero is not allowed.")
    elif choice == '5':
        print(f"\n{n1} % {n2} = {n1 % n2}")
    elif choice == '6':
        print(f"\n{n1} ** {n2} = {n1 ** n2}")
    else:
        print("\nInvalid input")
    choice2 = input("\nDo you want to perform another calculation? (yes/No): ").lower()


print("\nThank you for using the calculator. Goodbye!")
print("\nprogram ended\n")

'''part two'''
# A simple calculator that performs basic arithmetic operations
"""print("Welcome to the simple calculator!\n")

choice2 = "yes"
while choice2 in ["yes", "1"]:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    print("\nSelect operation:")
    print("1. Addition (+)") 
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")    
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")

    choice = input("\nEnter choice (1/2/3/4/5/6): ")

    # Perform calculation
    result = None
    if choice == '1':
        result = n1 + n2
        symbol = "+"
    elif choice == '2':
        result = n1 - n2
        symbol = "-"
    elif choice == '3':
        result = n1 * n2
        symbol = "*"
    elif choice == '4':
        if n2 != 0:
            result = n1 / n2
            symbol = "/"
        else:
            print("\nError: Division by zero is not allowed.")
    elif choice == '5':
        result = n1 % n2
        symbol = "%"
    elif choice == '6':
        result = n1 ** n2
        symbol = "**"
    else:
        print("\nInvalid input")

    # Print result neatly (no .0 if it's an integer)
    if result is not None:
        if result.is_integer():
            result = int(result)  # Convert to int if whole number
        print(f"\n{n1} {symbol} {n2} = {result}")

    print("-" * 40)
    choice2 = input("\nDo you want to perform another calculation? (yes/1 for yes, no/2 for no): ").lower()

print("\nThank you for using the calculator. Goodbye!")
print("\nProgram ended.\n")"""
