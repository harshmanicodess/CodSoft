def calc(a, b, ch):
    if ch == "1":
        print("Sum is:", a + b)
    elif ch == "2":
        print("Difference is:", a - b)
    elif ch == "3":
        print("Product is:", a * b)
    elif ch == "4":
        print("Division is:", a / b)
    else:
        print("You entered an invalid operator")

def main():
    while True:
        print("\nChoose operation:")
        print("1. Sum")
        print("2. Difference")
        print("3. Product")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        calc(a, b, choice)

if __name__ == "__main__":
    main()
