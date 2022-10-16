"""
ABC195 B
"""
a, b, w = map(int, input().split())
w *= 1000
min_count = w
max_count = -1
for i in range(1, w+1):
    left = a * i
    right = b * i
    if left <= w <= right:
        min_count = min(i, min_count)
        max_count = max(i, max_count)
print("UNSATISFIABLE" if max_count == -1 else f"{min_count} {max_count}")
