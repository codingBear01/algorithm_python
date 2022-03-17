arr = []

for i in range(10):
    nums = int(input())
    arr.append(nums % 42)

"""
result = []

for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])

print(len(result))
"""

result = set(arr)

print(len(result))
