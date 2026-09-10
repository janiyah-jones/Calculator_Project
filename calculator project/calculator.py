def calculate(operation, num1, num2):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 == 0:
            return "Answer is undefined"
        return num1 / num2


def main():
    calculator = True

    while calculator:
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Pick an option: ")

        if choice == "5":
            calculator = False
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "4" and num2 == 0:
            print("Answer is undefined")
            continue
        elif choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            result = num1 / num2

        print(result)


if __name__ == "__main__":
    main()