N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
for a, b, in zip(A, B):
    result += a * b

if result == 0:
    print("Yes")
else:
    print("No")
