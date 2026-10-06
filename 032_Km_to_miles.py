choice = input("Distance in (K)ilometers or Distance in (M)iles : ").lower()
dist = float(input("Enter the distance: "))

if choice == "k":
    miles  = dist / 1.60934
    print(f"{dist} kilometers is equal to {miles:.2f} miles.")
elif choice == "m":
    kilometers = dist * 1.60934
    print(f"{dist} miles is equal to {kilometers:.2f} kilometers.")
else:
    print("Invalid choice. Please enter 'K' for kilometers or 'M' for miles.")
