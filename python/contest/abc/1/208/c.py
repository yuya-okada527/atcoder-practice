N, K = map(int, input().split())
A = list(map(int, input().split()))

num, amari = K // N, K % N

sorted_a = sorted(A)

d = {}
