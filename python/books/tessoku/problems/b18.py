n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i == j == 0: DP[i][j] = True
        elif i == 0: DP[i][j] = False
        else:
            if DP[i-1][j]: DP[i][j] = True
            elif A[i] <= j and DP[i-1][j-A[i]]: DP[i][j] = True
            else: DP[i][j] = False
if not DP[-1][-1]:
    print(-1)
    exit()
cur = j
choice = []
for i in range(n, -1, -1):
    if DP[i-1][j]: continue
    choice.append(i)
    cur -= A[i]
print(len(choice))
print(*choice[::-1], sep=" ")
