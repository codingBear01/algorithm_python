inputN = input()


def hansu(num):
    strNum = str(num)

    if len(strNum) <= 2:
        return True

    diff = int(strNum[1]) - int(strNum[0])
    beforeNum = int(strNum[1])

    for i in range(2, len(strNum)):
        if int(strNum[i]) - beforeNum != diff:
            return False
        beforeNum = int(strNum[i])
    return True


def solution(N):
    cnt = 0
    for i in range(1, int(N) + 1):
        if hansu(i):
            cnt += 1
    print(cnt)


solution(inputN)
