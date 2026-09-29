nums = [1,2,3,4,5,6,7,8,9]

rev = []

for i in range(len(nums)-1, -1,-1):
    rev.append(nums[i])

print(rev)