N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

left = []
for a, b in zip(A, B):
    if len(left) == 0:
        left.append(a / b)
    else:
        left.append(left[-1] + a / b)

right = []
for a, b in zip(A[::-1], B[::-1]):
    if len(right) == 0:
        right.append(a / b)
    else:
        right.append(right[-1] + a / b)
right = right[::-1]

def calc_x(left, right):
    for i, l in enumerate(left):
        for r in right[::-1]:
            if l > r:
                return i
    return 0
x = calc_x(left, right)

left_start = left[x-1] if x != 0 else 0
right_start = right[x+1] if x != N-1 else 0
res = A[x] - abs(left_start-right_start) * B[x]
ans = 0
for i in range(x):
    ans += A[i]
if left_start < right_start:
    ans += abs(left_start-right_start) * B[x]
ans += res/2
print(ans)
