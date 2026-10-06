Salad = 5.99
Soup = 3.99
Chicken = 8.99
Total_Bill = 0.00
while True:
    print("1. Salad \n2. Soup \n3. Chicken \n4. Exit")

    choice = input("Choose: ")
    if choice == "1":
        print(f"Salad: ${Salad:.2f}")
        Total_Bill += Salad
    elif choice == "2":
        print(f"Soup: ${Soup:.2f}")
        Total_Bill += Soup
    elif choice == "3":
        print(f"Chicken: ${Chicken:.2f}")
        Total_Bill += Chicken
    elif choice == "4":
        print(f"Thank you for dining with us! \nYour Total Bill is: ${Total_Bill:.2f}")
        break
    else:
        print("Invalid choice. Please try again.")
