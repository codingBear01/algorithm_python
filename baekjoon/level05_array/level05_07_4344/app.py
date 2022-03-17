c = int(input())

grades = []

for i in range(c):
    grades.append(list(map(int, input().split())))

for i in range(c):
    n = grades[i][0]
    sum = 0

    for j in range(1, len(grades[i])):
        sum += grades[i][j]

    avg = sum / n
    cnt = 0

    for k in range(1, len(grades[i])):
        if grades[i][k] > avg:
            cnt += 1

    result = cnt / n * 100

    print("{:.3f}%".format(result))
