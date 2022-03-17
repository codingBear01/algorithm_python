t = int(input())

ox = []

for i in range(t):
    ox.append(list(input()))

for i in range(t):
    cnt = 0
    sum = 0

    for j in ox[i]:
        if j == "O":
            cnt += 1
        else:
            cnt = 0

        sum += cnt

    print(sum)
