p = float(input("Principal amount: "))
r = float(input("Rate of interest (%): "))
n = float(input("Time (in Years): "))

r = r/100

simple_interest = p * r * n
print("Simple Interest: ", simple_interest)