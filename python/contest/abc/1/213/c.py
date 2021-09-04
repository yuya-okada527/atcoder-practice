H, W, N = map(int, input().split())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A_dict = {a: i+1 for i, a in enumerate(sorted(list(set(A))))}
B_dict = {b: i+1 for i, b in enumerate(sorted(list(set(B))))}

for i in range(N):
    print(A_dict[A[i]], B_dict[B[i]])