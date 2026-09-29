nums = [1,5,4,3,5,7,8,7,4,8,6,1,4,52,5,7,89,4,58,7,41,5,7]

target = int(input("Enter the number to count occurrences: "))

count = 0

for i in nums:
    if i == target:
        count += 1

print("Count: ", count)