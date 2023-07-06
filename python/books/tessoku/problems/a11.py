import unittest
from pprint import pprint

def bs(x, array):
    l, r = 0, len(array)
    m = (l+r)//2
    while l < r:
        if array[m] > x: r = m
        else: l = m + 1
        m = (l+r)//2
    return l

def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    print(bs(x, A))


class Test(unittest.TestCase):
    def test_sample(self):
        x = 47
        array = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
        self.assertEqual(bs(x, array), 11)

    def test_left_edge(self):
        x = 3
        array = [3, 5, 7]
        self.assertEqual(bs(x, array), 1)

    def test_right_edge(self):
        x = 11
        array = [3, 4, 5, 11]
        self.assertEqual(bs(x, array), 4)

if __name__ == "__main__":
    # unittest.main()
    main()
