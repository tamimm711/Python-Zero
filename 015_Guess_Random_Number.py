import random

secret = random.randint(1,10)

guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct")
else:
    print(f"Wrong, it was {secret}")
