"""
abc143 C
例: aaabbcadd -> abcad
"""
n = int(input())
s = input()
ans = ""
i = 0
while i < n:
    j = i + 1
    while j < n and s[i] == s[j]:
        j += 1
    ans += s[i]
    i = j
print(len(ans))
