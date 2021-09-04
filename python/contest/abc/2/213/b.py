n = int(input())
A = list(map(int, input().split()))
score = sorted(A)[-2]
print(A.index(score)+1)