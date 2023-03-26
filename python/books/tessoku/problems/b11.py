def f(x, lst):
    left = 0
    right = len(lst)
    while left < right:
        mid = (left+right)//2
        if lst[mid] == x: return mid
        elif lst[mid] > x: right = mid
        else: left = mid + 1
    return left

n = int(input())
A = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    x = int(input())
    print(f(x, A))
