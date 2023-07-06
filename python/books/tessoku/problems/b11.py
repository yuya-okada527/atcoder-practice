import unittest

def bs(x, array):
    l, r = 0, len(array)
    while l < r:
        m = (l+r)//2
        if array[m] > x: r = m
        elif array[m] < x: l = m + 1
        else: return m
    return l

def main():
    n = int(input())
    A = list(sorted(map(int, input().split())))
    ans = []
    for _ in range(int(input())):
        x = int(input())
        ans.append(bs(x, A))
    for a in ans: print(a)


class Test(unittest.TestCase):
    def test_just(self):
        x = 3
        array = [1, 2, 3, 4]
        self.assertEqual(bs(x, array), 2)

    def test_not_just(self):
        x = 3.3
        array = [1, 2, 3, 4]
        self.assertEqual(bs(x, array), 3)

    def test_left(self):
        x = 1
        array = [1, 2, 3, 4]
        self.assertEqual(bs(x, array), 0)

    def test_right(self):
        x = 4.1
        array = [1, 2, 3, 4]
        self.assertEqual(bs(x, array), 4)


if __name__ == "__main__":
    # unittest.main()
    main()
