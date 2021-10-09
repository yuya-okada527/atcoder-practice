N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]
state = 0
X *= 100
for i, (v, p) in enumerate(VP, start=1):
    state += v * p
    if state > X:
        print(i)
        exit()
print(-1)
