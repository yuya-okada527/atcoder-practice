N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

prev_a, prev_b = A[0], B[0]
pattern = prev_b - prev_a + 1
for i in range(1, N):
    current_a, current_b = A[i], B[i]
    if current_a - prev_b >= 0:
        pattern *= current_b - current_a + 1
    else:
        pattern += (prev_b - prev_a + 1 - (prev_b - current_a)) * (current_b - current_a + 1) + (prev_b - current_a) * ((current_b - current_a + 1) - (prev_b - current_a))
print(pattern % 998244353)
