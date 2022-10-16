n = int(input())
s = input()
ans = 0
for i in range(n):
    x, y = s[i:], s[:i]
    ans = max(len(set(x) & set(y)), ans)
print(ans)
