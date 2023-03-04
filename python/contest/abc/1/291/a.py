s = input()
for i, x in enumerate(s, start=1):
    if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i)
