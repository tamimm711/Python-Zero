choice = input("Enter temperature unit to convert from (C/F): ").upper()

temp = float(input("Enter temperature: "))

# C to F
new_temp_f = (temp * 9/5) + 32

# F to C
new_temp_c = (temp - 32) * 5/9

if choice == "C":
    print(f"{temp}°C is equal to {new_temp_f}°F")
elif choice == "F":
    print(f"{temp}°F is equal to {new_temp_c}°C")
else:
    print("Invalid input. Please enter either 'C' or 'F'.")