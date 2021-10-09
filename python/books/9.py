N = int(input())
ans = 0
for i in range(1, N+1):
    ans += "7" not in str(i) and "7" not in str(oct(i))
print(ans)
