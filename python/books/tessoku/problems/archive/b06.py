n = int(input())
A = list(map(int, input().split()))
q = int(input())
LR = []
for _ in range(q):
    l, r = map(int, input().split())
    LR.append((l, r))
cums = [0]
for i in range(n):
    cums.append(cums[i] + A[i])
for l, r in LR:
    num = r - l + 1
    n_win = cums[r] - cums[l-1]
    n_lose = num - n_win
    if n_win == n_lose:
        print("draw")
    elif n_win > n_lose:
        print("win")
    else:
        print("lose")
