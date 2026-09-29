nums = [1,5,4,3,5,7,8,7,4,8,6,1,4,52,5,7,89,4,58,7,41,5,7]

unique_list = []

for i in nums:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)