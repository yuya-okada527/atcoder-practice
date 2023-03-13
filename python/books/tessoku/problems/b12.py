n = int(input())
left = 0
right = 10**3
for _ in range(100):
    mid = (left+right)/2
    ans = mid**3+mid
    if ans == n: break
    elif ans > n: right = mid
    else: left = mid
print(mid)
