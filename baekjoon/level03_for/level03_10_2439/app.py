n = int(input())

star = ""
space = ""
for i in range(n):
    star += "*"
    for j in range(n - i - 1, 0, -1):
        space += " "
    print(space + star)
    space = ""
