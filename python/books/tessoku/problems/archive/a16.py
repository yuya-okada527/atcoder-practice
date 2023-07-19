n = int(input())
A = [0] * 2 + list(map(int, input().split()))
B = [0] * 3 + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2: DP[i] = A[i]
    else: DP[i] = min(DP[i-1]+A[i], DP[i-2]+B[i])
print(DP[-1])
