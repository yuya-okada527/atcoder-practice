X, K, D = map(int, input().split())

if abs(X) >= K * D:
    print(abs(X) - K * D)
    exit()
K -= abs(X) // D
if K % 2 == 0:
    print(abs(X) % D)
else:
    print(D - (abs(X)%D))
