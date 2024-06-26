length = int(input("Enter the size of the pattern: "))
row_length = 1
while row_length <= length:
    column = 1
    while column <=length:
        print("*", end="")
        column +=1
    print()
    row_length+=1