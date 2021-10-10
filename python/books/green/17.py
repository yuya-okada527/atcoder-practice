N = int(input())
temp = set()
for a in range(2, 10**5+10):
    for b in range(2, 35):
        if a ** b <= N:
            temp.add(a**b)
        else:
            break
print(N-len(temp))
