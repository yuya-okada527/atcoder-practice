n, q = map(int, input().split())
players = [0 for _ in range(n+1)]
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        players[x] += 1
    elif c == 2:
        players[x] += 2
    else:
        if players[x] >= 2:
            print("Yes")
        else:
            print("No")
