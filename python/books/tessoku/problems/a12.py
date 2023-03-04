n, k = map(int, input().split())
A = list(map(int, input().split()))
left = 1
right = 10**9+1
while left < right:
    mid = (left+right)//2
    num = sum(map(lambda x: mid//x, A))
    if num >= k: right = mid
    else: left = mid + 1
print(left)
