N = int(input())
A = list(map(int, input().split()))

A_with_index = [(A[i], i) for i in range(N)]

print(sorted(A_with_index)[-2][1] + 1)