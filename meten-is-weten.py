a = int(input("A variable: "))
b = int(input("B variable: "))

if a > b:
    max = a
    print("A is het grootste getal: " + str(max))
elif a < b:
    min = a
    print("A is het kleinste getal: " + str(min))
else:
    print("A en B zijn even groot")