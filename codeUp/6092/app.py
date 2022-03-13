n = int(input())
nums = input().split()

for i in range(n):
    nums[i] = int(nums[i])

arr = []
for i in range(24):
    arr.append(0)

for i in range(n):
    arr[nums[i]] += 1

for i in range(1, 24):
    print(arr[i], end=" ")
