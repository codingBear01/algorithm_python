n = int(input())
nums = list(map(int, input().split()))

max = nums[0]

for num in nums:
    if max < num:
        max = num

sum = 0

for num in nums:
    sum += num / max * 100

print(sum / n)
