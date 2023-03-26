n = int(input())
H = [0] + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2: DP[i] = abs(H[i-1]-H[i])
    else: DP[i] = min(DP[i-1]+abs(H[i-1]-H[i]), DP[i-2]+abs(H[i-2]-H[i]))
pos = n
path = [n]
while True:
    if pos == 1: break
    if DP[pos-1]+abs(H[pos-1]-H[pos]) == DP[pos]: pos -= 1
    else: pos -= 2
    path.append(pos)

print(len(path))
print(*path[::-1], sep=" ")
