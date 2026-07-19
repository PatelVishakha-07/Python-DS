nums = [2, 7, 9, 3, 1]
prev = nums[0]
prev1 = max(prev, nums[1])

for i in range(2, len(nums)):
    m = max(prev + nums[i], prev1)

    prev = prev1
    prev1 = m

print(m)