import unittest

def f(n):
    l, r = 0, 10**4 + 100
    while l < r:
        m = (l+r)/2
        if abs(m**3+m - n) < 0.001: return m
        elif m**3+m >= n: r = m
        else: l = m
    return l

def main():
    n = int(input())
    print(f(n))


class Test(unittest.TestCase):
    def test_sample(self):
        n = 2
        self.assertTrue(abs(f(n)-1) <= 0.001)

    def test_sample2(self):
        n = 10
        self.assertTrue(abs(f(n)-2) <= 0.001)

    def test_sample3(self):
        n = 9
        self.assertTrue(abs(f(n)-1.920) <= 0.001)

if __name__ == "__main__":
    # unittest.main()
    main()
