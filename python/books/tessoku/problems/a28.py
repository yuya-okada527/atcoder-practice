n = int(input())
Q = [input().split() for _ in range(n)]
ans = 0
for t, a in Q:
    a = int(a)
    if t == "+":
        ans += a
    elif t == "*":
        ans *= a
    elif t == "-":
        ans -= a
    if ans < 0: ans += 10000
    ans %= 10000
    print(ans)
