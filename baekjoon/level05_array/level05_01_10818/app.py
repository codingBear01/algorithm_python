n = int(input())
array = list(map(int, input().split()))

"""
min = array[0]
max = array[0]

for num in array:
    if min > num:
        min = num
    elif max < num:
        max = num

print(min, max)
"""

print(min(array), max(array))
