text = input("Text: ").lower()
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Vowels:", count)
