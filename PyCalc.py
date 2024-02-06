def add(x, y):
    # input x is an integer
    # input y is an integer
    return x + y
    # output is an integer


def subtract(x, y):
    # input x is an integer
    # input y is an integer
    return x - y
    # output is an integer


def multiply(x, y):
    # input x is an integer
    # input y is an integer
    return x * y
    # output is an integer


def divide(x, y):
    # input x is an integer
    # input y is an integer =/= 0
    if y == 0:
        return "Cannot Divide by 0"
    return x / y
    # output is an integer


def square(x):
    # input is an integer
    return x * x
    # output is an integer


def sqrt(x):
    # input is an integer > 0
    if x < 0:
        return "Cannot root a negative number"
    elif x == 0:
        return 0
        # output is an integer 0
    else:
        return x**0.5
        # output is an integer > 0


running = True


while running:

    print("Select operation:")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Division")
    print("6. Square")
    print("7. Square Root\n")
    print("0. Quit\n")

    while True:
        choice = int(input("Enter choice number: "))

        if choice <= 8 and choice > -1:
            if choice == 2:
                num1 = float(input("Add: "))
                num2 = float(input("To: "))
                print("Result:", add(num1, num2))
            elif choice == 3:
                num1 = float(input("Subtract: "))
                num2 = float(input("From: "))
                print("Result:", subtract(num1, num2))
            elif choice == 4:
                num1 = float(input("Multiply: "))
                num2 = float(input("By: "))
                print("Result:", multiply(num1, num2))
            elif choice == 5:
                num1 = float(input("Divide: "))
                num2 = float(input("By: "))
                print("Result:", divide(num1, num2))
            elif choice == 6:
                num1 = float(input("Square: "))
                print("Result:", square(num1))
            elif choice == 7:
                num1 = float(input("Root: "))
                print("Result:", sqrt(num1))
            elif choice == 0:
                running = False
            break
        else:
            print("Invalid Input")
