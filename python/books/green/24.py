N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

ans = 10 ** 20
for i in range(1<<N):
    cost = 0
    skill = [0] * M
    for book in range(N):
        if i >> book & 1 == 1:
            cost += C[book]
            for j in range(M):
                skill[j] += A[book][j]
    if X <= min(skill):
        ans = min(ans, cost)
if ans == 10 ** 20:
    print(-1)
else:
    print(ans)
