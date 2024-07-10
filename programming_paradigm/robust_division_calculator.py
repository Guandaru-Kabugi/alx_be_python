def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if numerator == 0 or denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            results = (numerator)/(denominator)
            print (f"The result of the division is {results}")
    except ValueError:
        return "Error: Please enter numeric values only."
    except (ZeroDivisionError,ValueError) as e:
        print(e)
    