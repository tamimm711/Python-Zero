a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = float(input("Enter the 3rd number: "))

if a > b and a > c:
    print("Maximum number is a:", a)
elif b > a and b > c:
    print("Maximum number is b:", b)
else:
    print("Maximum number is c:", c)
