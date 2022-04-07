# def d(num):
#     sum = num
#     while True:
#         if num == 0:
#             break
#         sum += num % 10
#         num = int(num / 10)
#     return sum


# """
# notSelfNum(33):
# 1. sum = 33
# 2. sum = 33 + 3 => 36
# 3. num = 3
# 4. sum = 36 + 3 => 39
# 5. num = 0 (int(3 / 10) => 0)
# 6. num == 0 => break
# 7. return sum => 39
# """


# def solution(num):
#     notSelfNum = []

#     for i in range(1, num + 1):
#         nums = d(i)

#         notSelfNum.append(nums)

#     for j in range(1, num + 1):
#         if j in notSelfNum:
#             pass
#         else:
#             print(j)


# solution(10000)

nums = set(range(1, 10001))

notSelfNum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)

    notSelfNum.add(i)

selfNum = nums - notSelfNum

for i in sorted(selfNum):
    print(i)
