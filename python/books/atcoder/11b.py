n = int(input())
s = input()
ans = 0
for i in range(1, n):
    x = set(s[:i])
    y = set(s[i:])
    ans = max(ans, len(x & y))
print(ans)
