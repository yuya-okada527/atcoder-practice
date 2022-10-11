UPPER = 10**18

a, b, c, k = map(int, input().split())
if k % 2 != 0:
    if abs(b-a) > UPPER:
        print("Unfair")
    else:
        print(b-a)
else:
    if (a-b) > UPPER:
        print("Unfair")
    else:
        print(a-b)
