"""
abc139 C
ex. 10 4 8 7 3 -> 1 2
"""
def f(lst):
    n = len(lst)
    count = []
    i = 0
    while i < n:
        j = i + 1
        c = 0
        while j < n and lst[i] >= lst[j]:
            j += 1
            c += 1
            i += 1
        count.append(c)
        i = j
    return max(count)


def main():
    n = int(input())
    H = list(map(int, input().split()))
    print(f(H))


def test():
    case = [

    ]
    for c in case:
        assert f(c[0]) == c[1]


main()
