
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


contents = """
------------------------------------------------
-----Main Menu-----
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
------------------------------------------------
"""

continue_loop = True

while continue_loop:
    print(contents)
    try:
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Thank you for using our calculator!")
            continue_loop = False
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print(f"Sum of {a} and {b} is {add(a, b)}")
        elif choice == "2":
            print(f"Difference of {a} and {b} is {sub(a, b)}")
        elif choice == "3":
            print(f"Product of {a} and {b} is {mul(a, b)}")
        elif choice == "4":
            print(f"Division of {a} and {b} is {div(a, b)}")
        else:
            print("Please provide a valid choice!")
        print()
    except ValueError:
        print("Please provide a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print("Something went wrong!")
