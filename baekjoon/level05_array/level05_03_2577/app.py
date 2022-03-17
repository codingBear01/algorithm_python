a = int(input())
b = int(input())
c = int(input())

mul = list(str(a * b * c))

# arr = [0 for _ in range(10)]

# for i in range(len(arr)):
#     for j in range(len(mul)):
#         if i == int(mul[j]):
#             arr[i] += 1
#     print(arr[i])

for i in range(10):
    cnt = 0
    for j in range(len(mul)):
        if i == int(mul[j]):
            cnt += 1
    print(cnt)
