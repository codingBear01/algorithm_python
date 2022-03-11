hz, bit, ch, sc = input().split()
hz = int(hz)
bit = int(bit)
ch = int(ch)
sc = int(sc)

print(format(hz * bit * ch * sc / 8 / 1024 / 1024, ".1f"), "MB")
