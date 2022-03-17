"""
nums = []
for i in range(9):
    nums.append(int(input()))

max = nums[0]
idx = 0

for i in range(len(nums)):
    if max < nums[i]:
        max = nums[i]
        idx = i

print(max)
print(idx + 1)
"""

nums = [int(input()) for _ in range(9)]

print(max(nums))
print(nums.index(max(nums)) + 1)
