FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f"{fahrenheit}°F is {celsius}°C")
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32 
    print(f"{celsius}°C is {fahrenheit}°F")
temperature_to_convert = float(input("Enter the temperature to convert: "))
format_of_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
match format_of_temperature:
    case 'c':
        convert_to_fahrenheit(temperature_to_convert)
    case 'f':
        convert_to_celsius(temperature_to_convert)
    case _:
        print("Invalid temperature. Please enter a numeric value.")