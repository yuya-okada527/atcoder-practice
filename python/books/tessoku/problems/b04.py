n = input()
length = len(n)
ans = 0
for i, j in enumerate(n, start=1):
    if j == "1":
        ans += 2**(length-i)
print(ans)
