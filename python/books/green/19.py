import pdb

X, K, D = map(int, input().split())

abs_x = abs(X)

if abs_x > K * D:
    print(abs_x - K * D)
else:
    if abs_x <= D:
        if K % 2 == 0:
            print(abs_x)
        else:
            print(D - abs_x)
    else:
        k = abs_x // D
        abs_x -= D * k
        if (K-k) % 2 == 0:
            print(abs_x)
        else:
            print(D-abs_x)
# pdb.set_trace()
