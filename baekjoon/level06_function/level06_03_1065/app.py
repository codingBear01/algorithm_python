# inputN = input()


# def hansu(num):
#     strNum = str(num)

#     if len(strNum) <= 2:
#         return True

#     diff = int(strNum[1]) - int(strNum[0])
#     beforeNum = int(strNum[1])

#     for i in range(2, len(strNum)):
#         if int(strNum[i]) - beforeNum != diff:
#             return False
#         beforeNum = int(strNum[i])
#     return True


# def solution(N):
#     cnt = 0
#     for i in range(1, int(N) + 1):
#         if hansu(i):
#             cnt += 1
#     print(cnt)


# solution(inputN)


num = int(input())


def hansu(n):
    cnt = 0
    for i in range(1, n + 1):
        hundred = i // 100
        ten = (i - 100 * hundred) // 10
        one = i % 10

        if i <= 99:
            cnt += 1
        elif 100 <= i and i < 1000:
            if hundred - ten == ten - one:
                cnt += 1
    return cnt


print(hansu(num))
