n = int(input())
A = [0, 0] + list(map(int, input().split()))
B = [0, 0, 0] + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1: DP[i] = 0
    elif i == 2: DP[i] = A[i]
    else: DP[i] = min(DP[i-1]+A[i], DP[i-2]+B[i])
path = []
point = n
while True:
    path.append(point)
    if DP[point] == DP[point-1] + A[point]:
        point -= 1
    else:
        point -= 2
    if point == 1:
        path.append(point)
        break
print(len(path))
print(*path[::-1], sep=" ")
