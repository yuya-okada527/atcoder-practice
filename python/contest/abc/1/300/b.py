from pprint import pprint as pp
from copy import deepcopy

def is_same(a, b):
    for i in range(h):
        for j in range(w):
            if a[i][j] != b[i][j]:
                return False
    return True


def shift_verticaly(a):
    b = [["" for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            b[i][(j+1)%w] = a[i][j]
    return b


def shift_horizontaly(a):
    b = [["" for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            b[(i+1)%h][j] = a[i][j]
    return b


def judge(a, b):
    for i in range(h):
        # print(f"{i=}")
        copy_a = deepcopy(a)
        while True:
            if i == 0: break
            copy_a = shift_verticaly(copy_a)
            i -= 1
        for j in range(w):
            # print(f"{j=}")
            copy_a2 = deepcopy(copy_a)
            while True:
                if j == 0: break
                copy_a2 = shift_horizontaly(copy_a2)
                j -= 1
            # pp(copy_a2)
            if is_same(copy_a2, b):
                return True
    return False


h, w = map(int, input().split())
A = [[i for i in input()] for _ in range(h)]
B = [[i for i in input()] for _ in range(h)]
if judge(A, B):
    print("Yes")
else:
    print("No")
