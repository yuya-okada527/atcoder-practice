from bisect import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

ans = 10**9+1
for a in A:
    index = bisect(B, a)
    if index == 0:
        ans = min(ans, B[index] - a)
    elif index == M:
        ans = min(ans, a - B[index-1])
    else:
        ans = min(ans, abs(B[index] - a), abs(B[index-1] - a))

print(ans)