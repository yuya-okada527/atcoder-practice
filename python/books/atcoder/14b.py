"""
abc19 b
ex. aabbbaad -> a2b3a2d1
"""
s = input()
n = len(s)
ans = ""
i = 0
while i < n:
    count = 1
    j = i + 1
    while j < n and s[i] == s[j]:
        j += 1
        count += 1
    ans += s[i] + str(count)
    i = j
print(ans)
