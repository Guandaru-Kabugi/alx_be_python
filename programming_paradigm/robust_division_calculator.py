# def safe_divide(numerator, denominator):
#     try:
#         numerator = float(numerator)
#         denominator = float(denominator)
#         if not  isinstance (numerator,(int, float)) or not isinstance (denominator,(int,float)):
#             raise ValueError("Error: Please enter numeric values only.")
            
#         if numerator == 0 or denominator == 0:
#             raise ZeroDivisionError("Error: Cannot divide by zero.")
#         else:
#             results = (numerator)/(denominator)
#             return (f"The result of the division is {results}")
#     except ValueError:
#         return "Error: Please enter numeric values only."
#     except (ZeroDivisionError,ValueError) as e:
#         return e

def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if not  isinstance (numerator,(int, float)) or not isinstance (denominator,(int,float)):
            raise ValueError
            
        if numerator == 0 or denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            results = (numerator)/(denominator)
            return (f"The result of the division is {results}")
    except ValueError:
        return "Error: Please enter numeric values only."
    except (ZeroDivisionError,ValueError) as e:
        return e
    