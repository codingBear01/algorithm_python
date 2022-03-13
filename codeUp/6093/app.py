n = int(input())
nums = input().split()

for i in range(n - 1, -1, -1):
    print(nums[i], end=" ")
