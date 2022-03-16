inputNum = int(input())

tempNum = inputNum
sum = ""
cnt = 0

while True:
    sum = (tempNum // 10) + (tempNum % 10)
    tempNum = (tempNum % 10) * 10 + (sum % 10)
    cnt += 1

    if inputNum == tempNum:
        break

print(cnt)
