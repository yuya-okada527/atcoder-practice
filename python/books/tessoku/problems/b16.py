n = int(input())
H = [0] + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2: DP[i] = abs(H[1]-H[2])
    else: DP[i] = min(DP[i-1]+abs(H[i-1]-H[i]), DP[i-2]+abs(H[i-2]-H[i]))
print(DP[-1])
