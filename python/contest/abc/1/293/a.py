s = input()
ans = ""
odd = ""
even = ""
for i , string in enumerate(s, start=1):
    if i % 2 != 0: odd += string
    else: even += string
for o, e in zip(odd, even):
    ans += e + o
print(ans)
