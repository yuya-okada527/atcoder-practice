from typing import List
import unittest


def f(lst: List[int]):
    assert isinstance(lst, list)
    assert len(set(lst)) >= 2
    return sorted(set(lst))[-2]


def main():
    n = int(input())
    lst = map(int, input().split())
    ans = f(lst)
    print(ans)


class UnitTest(unittest.TestCase):
    def test_リスト以外の場合(self):
        not_list_args = [None, "string", 1, True, {}]
        for args in not_list_args:
            with self.assertRaises(AssertionError):
                f(args)

    def test_空配列の場合(self):
        with self.assertRaises(AssertionError):
            f([])

    def test_要素数1の配列の場合(self):
        with self.assertRaises(AssertionError):
            f([1])

    def test_要素数2の配列の場合(self):
        self.assertEqual(f([1, 2]), 1)

    def test_ソート済みの場合(self):
        self.assertEqual(f([1, 2, 3]), 2)

    def test_ソートされていない場合(self):
        self.assertEqual(f([6, 3, 1, 2]), 3)

    def test_重複あり_最高値(self):
        self.assertEqual(f([1, 2, 2]), 1)

    def test_重複あり_2番目(self):
        self.assertEqual(f([1, 1, 2]), 1)

    def test_全て同じ値(self):
        with self.assertRaises(AssertionError):
            f([1, 1, 1])


if __name__ == "__main__":
    unittest.main()
    # main()
