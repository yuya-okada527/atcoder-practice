h, w = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]

for a, b, c, d in Q:
    ans = 0
    for x in X[a-1:c] if c != h else X[a-1:]:
        ans += sum(x[b-1:d] if d != w else x[b-1:])
    print(ans)
