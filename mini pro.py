def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: divide by zero"
    return x / y


def calculator():
    while True:
        print("\n=== Dynamic Calculator ===")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Exit")

        choice = input("Select option (1-5): ").strip()

        if choice == '5':
            print("Bye!")
            break

        if choice not in ('1','2','3','4'):
            print("Invalid choice, try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", sub(a, b))
        elif choice == '3':
            print("Result:", mul(a, b))
        elif choice == '4':
            print("Result:", div(a, b))

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    calculator()
