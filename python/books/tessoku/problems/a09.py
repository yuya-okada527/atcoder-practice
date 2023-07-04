import unittest

def f(h, w, matrix):
    HW = [[0 for _ in range(w+2)] for _ in range(h+2)]
    Z  = [[0 for _ in range(w+2)] for _ in range(h+2)]
    for a, b, c, d in matrix:
        HW[a][b]     += 1
        HW[a][d+1]   -= 1
        HW[c+1][b]   -= 1
        HW[c+1][d+1] += 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            Z[i][j] = Z[i-1][j] + HW[i][j]
    for i in range(1, h+1):
        for j in range(1, w+1):
            Z[i][j] = Z[i][j-1] + Z[i][j]
    return [z[1:-1] for z in Z[1:-1]]

def main():
    h, w, n = map(int, input().split())
    matrix = [map(int, input().split()) for _ in range(n)]
    for z in f(h, w, matrix):
        print(*z, sep=" ")

class Test(unittest.TestCase):
    def test_sample(self):
        args = [5, 5, [[1, 1, 3, 3], [2, 2, 4, 4]]]
        expected = [
            [1, 1, 1, 0, 0],
            [1, 2, 2, 1, 0],
            [1, 2, 2, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(f(*args), expected)

    def test_minimum(self):
        args = [1, 1, [[1, 1, 1, 1], [1, 1, 1, 1]]]
        expected = [
            [2]
        ]
        self.assertEqual(f(*args), expected)

    def test_maximum(self):
        args = [1500, 1500, [[1, 1, 1500, 1500] for _ in range(100000)]]
        expected = [[100000 for _ in range(1500)] for _ in range(1500)]
        self.assertEqual(f(*args), expected)

    def test_rectangle(self):
        args = [1, 2, [[1, 1, 1, 2]]]
        expected = [
            [1, 1]
        ]
        self.assertEqual(f(*args), expected)

if __name__ == "__main__":
    # unittest.main()
    main()
