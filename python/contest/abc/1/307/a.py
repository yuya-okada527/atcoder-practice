n = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append(sum(A[i*7:(i+1)*7]))
print(*ans, sep=" ")
