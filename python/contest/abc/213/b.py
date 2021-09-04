N = int(input())
A = list(map(int, input().split()))

rank = sorted(A)

print(A.index(rank[-2])+1)