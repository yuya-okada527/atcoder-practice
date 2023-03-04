n = int(input())
X = sorted(list(map(int, input().split())))
print(sum(X[n:-n]) / (3*n))
