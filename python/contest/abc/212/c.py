from bisect import bisect

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 10**9 + 1
for a in A:
    index = bisect(B, a)
    if index == 0:
        ans = min(ans, abs(a - B[index]))
    elif index == M:
        ans = min(ans, abs(a - B[index-1]))
    else:
        ans = min(ans, abs(a - B[index]), abs(a - B[index-1]))

print(ans)
