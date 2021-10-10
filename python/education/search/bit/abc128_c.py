N, M = map(int, input().split())
K = []
S = []
for _ in range(M):
    KS = list(map(int, input().split()))
    K.append(KS[0])
    S.append(KS[1:])
P = list(map(int, input().split()))

for i in range(1<<N):
    lights = [0] * M
    for switch in range(N):
        if i>>swhich & 1 == 1:
            for j in S[switch]:
                lights[j] += 1
    all_on = True
    for l, p in zip(lights, P):
        all_on &=
