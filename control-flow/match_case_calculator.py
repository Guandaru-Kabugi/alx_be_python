num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+" :
        results = (num1) + (num2)
        print(f"The result is: {results}")
    case "-":
        results = (num1) - (num2)
        print(f"The result is: {results}")
    case "*":
        results = (num1) * (num2)
        print(f"The result is: {results}")
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            results = (num1) / (num2)
            print(f"The result is: {results}")