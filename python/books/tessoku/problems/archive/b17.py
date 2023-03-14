n = int(input())
H = [0] + list(map(int, input().split()))
DP = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1: DP[i] = 0
    elif i == 2: DP[i] = abs(H[i-1]-H[i])
    else: DP[i] = min(
        DP[i-1] + abs(H[i-1]-H[i]),
        DP[i-2] + abs(H[i-2]-H[i])
    )
path = []
place = n
while True:
    path.append(place)
    if place == 1: break
    elif DP[place] == DP[place-1] + abs(H[place-1]-H[place]): place -= 1
    else: place -= 2
print(len(path))
print(*path[::-1], sep=" ")
