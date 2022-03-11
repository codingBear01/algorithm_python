a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print(not (c or d))
print(not c and not d)
