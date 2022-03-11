n = int(input())

if n >= 90:
    print("A")
else:
    if n >= 70:
        print("B")
    else:
        if n >= 40:
            print("C")
        else:
            print("D")

"""
if (n >= 90) and (n <= 100):
    print("A")
elif (n >= 70) and (n < 90):
    print("B")
elif (n >= 40) and (n < 70):
    print("C")
elif (n >= 0) and (n < 40):
    print("D")
"""
