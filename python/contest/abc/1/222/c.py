def janken(choice1, choice2):
    if choice1 == choice2:
        return 0, 0
    if choice1 == "G":
        if choice2 == "C":
            return 1, 0
        else:
            return 0, 1
    elif choice1 == "C":
        if choice2 == "P":
            return 1, 0
        else:
            return 0, 1
    else:
        if choice2 == "G":
            return 1, 0
        else:
            return 0, 1

N, M = map(int, input().split())
A = [input() for _ in range(2*N)]

ranks = [[i+1, 0] for i in range(2*N)]
for i in range(1, M+1):
    for k in range(1, N+1):
        idx1, idx2 = ranks[2*k-1-1][0], ranks[2*k-1][0]
        choice1, choice2 = A[idx1-1][i-1], A[idx2-1][i-1]
        result1, result2 = janken(choice1, choice2)
        ranks[2*k-1-1][1] += result1
        ranks[2*k-1][1] += result2
        ranks.sort(key=lambda x: x[0])
        ranks.sort(reverse=True, key=lambda x: x[1])
for r in ranks:
    print(r[0])
