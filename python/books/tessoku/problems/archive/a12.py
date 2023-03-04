n, k = map(int, input().split())
A = list(map(int, input().split()))
def f(i):
    total = sum(map(lambda x: i // x, A))
    return True if total >= k else False

left = 1
right = 10**9
while left < right:
    mid = (left+right) // 2
    check = f(mid)
    if check: right = mid
    else: left = mid + 1
print(left)
