N, K = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)])
friend_pos = 0
current_pos = K
for i in range(N):
    friend_pos = AB[i][0]
    if friend_pos <= current_pos:
        current_pos += AB[i][1]
print(current_pos)
