from pprint import pprint

def f(n, ABCD):
    # SIZE = 10
    SIZE = 1500 + 1
    MAP = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    CUM = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for a, b, c, d in ABCD:
        MAP[a][b]     += 1
        MAP[c][b]   -= 1
        MAP[a][d]   -= 1
        MAP[c][d] += 1
    for i in range(SIZE-1):
        for j in range(SIZE-1):
            if i == 0: CUM[i][j] = MAP[i][j]
            else: CUM[i][j] = CUM[i-1][j] + MAP[i][j]
    for i in range(SIZE-1):
        for j in range(SIZE-1):
            if j == 0: CUM[i][j] = CUM[i][j]
            else: CUM[i][j] += CUM[i][j-1]
    count = 0
    for c in CUM[:-1]:
        for num in c[:-1]:
            if num > 0: count += 1
    print(count)


def main():
    n = int(input())
    ABCD = [list(map(int, input().split())) for _ in range(n)]
    f(n, ABCD)


if __name__ == "__main__":
    # unittest.main()
    main()
