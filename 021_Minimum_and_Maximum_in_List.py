# nums = [1,5,8,5,45,65,4,0,7,21,58]
# mn = mx = nums[0]

# for i in nums:
#     if i < mn: mn = i
#     if i > mx: mx = i

# print(f"Min:, {mn}, Max:, {mx}")

nums = [1,5,8,5,45,65,4,0,7,21,58]
mn = mx = nums[0]
for x in nums:
    mn = min(mn, x)
    mx = max(mx, x)
print("Min:", mn, "Max:", mx)