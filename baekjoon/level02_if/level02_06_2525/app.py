h, m = map(int, input().split())
t = int(input())

time = h * 60 + m + t

if time >= 1440:
    time -= 1440

h = time // 60
m = time % 60

print(h, m)
