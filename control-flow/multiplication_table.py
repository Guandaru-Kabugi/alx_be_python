number = int(input("Enter a number to see its multiplication table: "))
for no in range (1,11):
    results = number * no
    print(f"{number} * {no} = {results}")