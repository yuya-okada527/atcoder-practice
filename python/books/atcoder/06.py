n = int(input())
A = list(map(int, input().split()))
ans = 0
while all([a % 2 == 0 for a in A]):
    ans += 1
    A = list(map(lambda x: x / 2, A))
print(ans)
