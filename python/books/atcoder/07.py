N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
alice, bob = 0, 0
for i, a in enumerate(A):
    if i % 2 == 0:
        alice += A[i]
    else:
        bob += A[i]
print(alice - bob)
