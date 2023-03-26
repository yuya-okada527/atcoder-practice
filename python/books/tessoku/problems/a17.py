n = int(input())
A = [0] * 2 + list(map(int, input().split()))
B = [0] * 3 + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2: DP[i] = A[i]
    else: DP[i] = min(DP[i-1]+A[i], DP[i-2]+B[i])
pos = n
path = [n]
while True:
    if pos == 1: break
    if DP[pos-1]+ A[pos] == DP[pos]: pos -= 1
    else: pos -= 2
    path.append(pos)

print(len(path))
print(*path[::-1], sep=" ")
