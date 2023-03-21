n = int(input())
ans = 0
Q = []
for _ in range(n):
    t, a = input().split()
    Q.append((t, a))
for t, a in Q:
    if t == "+": ans += int(a)
    elif t == "-": ans -= int(a)
    else: ans *= int(a)
    if ans < 0: ans += 10000
    ans %= 10000
    print(ans)
