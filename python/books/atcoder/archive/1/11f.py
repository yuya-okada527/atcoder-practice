import sys
input = sys.stdin.readline


def f(sc, target):
    for s, c in sc:
        if int(target[s-1]) != c:
            return False
    return True


def main():
    n, m = map(int, input().split())
    sc = []
    for _ in range(m):
        sc.append(tuple(map(int, input().split())))
    for i in range(1000):
        if len(str(i)) != n:
            continue
        target = str(i)
        if f(sc, target):
            print(target)
            return
    print(-1)


if __name__ == "__main__":
    main()
