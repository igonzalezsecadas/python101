while True:
    try:
        number1 = float(input("Input a number: "))
        number2 = float(input("Input a second number: "))
        operation = str(input("Select an operation(add / subtract / multiply / divide): "))

        match operation:
            case "add":
                print(number1 + number2)
            case "subtract":
                print(number1 - number2)
            case "multiply":
                print(number1 * number2)
            case "divide":
                try:
                    print(number1 / number2)
                except ZeroDivisionError as e:
                    print("You can't divide by zero")
            case "exit":
                print("Exiting program")
                break
            case _:
                print("Invalid operation")
    except ValueError as e:
        print("You have to input numbers")
        continue
