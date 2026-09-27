a = float(input(" a = "))
op = input("Operator (+, -, *, /): ")
b = float(input(" b = "))

if op == "+":
    print("Result:", a+b)
elif op == "-":
    print("Result:", a-b)
elif op == "*":
    print("Result:", a*b)
elif op == "/":
    if b==0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", a/b)
else:
    print("Error: Invalid operator!")