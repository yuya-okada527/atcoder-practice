N = int(input())
A = sorted(list(map(int, input().split())))
if A == list(range(1, N+1)):
    print("Yes")
else:
    print("No")
