import unittest


def bs(x, array):
    l, r = 1, 10**9 + 10
    while l < r:
        m = (l+r)//2
        if sum(map(lambda x: m // x, array)) >= x: r = m
        else: l = m + 1
    return l


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    print(bs(k, A))


class Test(unittest.TestCase):

    def test_sample(self):
        k = 10
        A = [1, 2, 3, 4]
        self.assertEqual(bs(k, A), 6)

    def test_just(self):
        k = 6
        A = [1, 1, 1]
        self.assertEqual(bs(k, A), 2)

    def test_first(self):
        k = 1
        A = [1, 2, 3, 4]
        self.assertEqual(bs(k, A), 1)

    def test_last(self):
        k = 10**9
        A = [1]
        self.assertEqual(bs(k, A), 10**9)


if __name__ == "__main__":
    # unittest.main()
    main()
