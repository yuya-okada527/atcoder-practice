# from pprint import pprint

n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i == 0 and j == 0: DP[i][j] = True
        elif i == 0: DP[i][j] = False
        elif DP[i-1][j]: DP[i][j] = True
        elif j >= A[i]:
            if DP[i-1][j-A[i]]:
                DP[i][j] = True
if not DP[-1][-1]:
    print(-1)
    exit()

path = []
position = s
for i in range(n, 0, -1):
    if DP[i-1][position]:
        continue
    path.append(i)
    position -= A[i]
print(len(path))
print(*path[::-1], sep=" ")
