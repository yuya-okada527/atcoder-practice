from pprint import pprint

n = int(input())
A = [0] + list(map(int, input().split()))
C = [0 for _ in range(n+1)]
for i in range(1, n+1): C[i] = C[i-1] + A[i]
q = int(input())
LR = [map(int, input().split()) for _ in range(q)]
for l, r in LR:
    n = r - l + 1
    win = C[r] - C[l-1]
    lose = n - win
    if win > lose: print("win")
    elif lose > win: print("lose")
    else: print("draw")
