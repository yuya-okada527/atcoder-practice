n, x = map(int, input().split())
A = list(map(int, input().split()))
left = 0
right = n
while left < right:
    mid = (left+right) // 2
    if A[mid] == x: break
    elif A[mid] > x: right = mid
    else: left = mid + 1
print(mid+1)
