from math import floor

n = int(input())
left = 1.0
right = 100.0
while left < right:
    mid = (left+right)//2
    result = mid**3 + mid
    if result == n * 1.0: break
    elif result > n: right = mid
    else: left = mid + 1
print(mid)
