n = int(input())
Q = [input().split() for _ in range(n)]
ans = 0
for t, a in Q:
    if t == "+":
        ans += int(a)
    elif t == "-":
        ans -= int(a)
    else:
        ans *= int(a)
    if ans < 0: ans += 10000
    ans %= 10000
    print(ans)
