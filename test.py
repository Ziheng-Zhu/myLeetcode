nums = [0,1,1,2,4,4,5,5,5]
n = len(nums)
ans = 0
nums.sort()
total = [nums[0]]

for i in range(1, n):
    val = nums[i]
    if val == nums[i - 1]:
        total[-1] += val
    elif val == nums[i - 1] + 1:
        total.append(val)
    else:
        total = [val]

print(total)