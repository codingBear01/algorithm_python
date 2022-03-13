n = int(input())
nums = input().split()

for i in range(n):
    nums[i] = int(nums[i])

min = nums[0]
for i in range(n):
    if min > nums[i]:
        min = nums[i]

print(min)
