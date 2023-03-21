n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
seq_a = []
seq_b = []
pos_a = 1
pos_b = 1
pos_c = 1
while True:
    if pos_a == n+1:
        seq_b.append(pos_c)
        pos_b += 1
    elif pos_b == m+1:
        seq_a.append(pos_c)
        pos_a += 1
    elif A[pos_a] < B[pos_b]:
        seq_a.append(pos_c)
        pos_a += 1
    else:
        seq_b.append(pos_c)
        pos_b += 1
    pos_c += 1
    if pos_a == n+1 and pos_b == m+1: break
print(*seq_a, sep=" ")
print(*seq_b, sep=" ")
