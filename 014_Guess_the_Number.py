secret = 7

guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct")
elif guess >= secret:
    print("Too High")
elif guess <= secret:
    print("Too low")
else:
    print("Invalid input")