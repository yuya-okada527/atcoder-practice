N, A, X, Y = map(int, input().split())

if N > A:
    print(X*A+Y*(N-A))
else:
    print(X*N)