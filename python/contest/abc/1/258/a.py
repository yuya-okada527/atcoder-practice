k = int(input())
if k >= 60:
    hh = 22
    mm = k - 60
else:
    hh = 21
    mm = k

print(f"{hh}:{mm:02}")
