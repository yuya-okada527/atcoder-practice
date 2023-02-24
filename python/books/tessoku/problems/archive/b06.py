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
# print(cums)
for j in range(q):
    l, r = LR[j]
    n_all = r - l + 1
    n_win = cums[r] - cums[l-1]
    n_lose = n_all - n_win
    # print(n_all, n_win, n_lose)
    if n_win > n_lose:
        print("win")
    elif n_win == n_lose:
        print("draw")
    else:
        print("lose")
