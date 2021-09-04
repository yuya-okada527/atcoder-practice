N = int(input())
names = set([input() for _ in range(N)])
if len(names) == N:
    print("No")
else:
    print("Yes")