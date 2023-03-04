n, x = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = n
while left < right:
    mid = (right - left) // 2 + left
    if A[mid] == x: break
    elif A[mid] > x: right = mid
    else: left = mid
print(mid+1)
