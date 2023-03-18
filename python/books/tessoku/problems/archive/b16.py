n = int(input())
H = [0] + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for j in range(1, n+1):
    if j == 1: DP[j] = 0
    elif j == 2: DP[j] = abs(H[j-1]-H[j])
    else: DP[j] = min(
        DP[j-1] + abs(H[j-1]-H[j]),
        DP[j-2] + abs(H[j-2]-H[j])
    )
print(DP[-1])
