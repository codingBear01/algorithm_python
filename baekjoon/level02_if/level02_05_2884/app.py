h, m = map(int, input().split())

# m -= 45

# if m >= 0:
#     print(h, m)
# elif h > 0 and m < 0:
#     print(h - 1, m + 60)
# else:
#     print(23, m + 60)

time = h * 60 + m - 45

h = time // 60
m = time % 60

if h < 0:
    print(h + 24, m)
else:
    print(h, m)
