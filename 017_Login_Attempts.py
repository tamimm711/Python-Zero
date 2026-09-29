correct = "python123"

for i in range(3):
    pword = input("Enter Password: ")
    if pword == correct:
        print("Welcome")
        break
else:
    print("Too many attempts!")
